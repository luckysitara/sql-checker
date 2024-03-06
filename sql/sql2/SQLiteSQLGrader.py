#!/usr/bin/python3
import sqlite3

class SQLiteSQLGrader:
    """
    SQLite SQL Grader class for evaluating student SQL queries against a lecturer's solution.
    """

    def __init__(self, sqlite_db):
        """
        Constructor for SQLiteSQLGrader.

        Parameters:
        - sqlite_db (str): SQLite database file path.
        """
        self.connection = sqlite3.connect(sqlite_db)

    def evaluate_student_sql(self, student_query):
        """
        Evaluate a student's SQL query against a lecturer's solution.

        Parameters:
        - student_query (str): SQL query provided by the student.

        Returns:
        - int: Score based on the evaluation.
        """
        try:
            with self.connection.cursor() as cursor:
                # Execute the lecturer's query
                cursor.execute('SELECT * FROM lecturer_solution')
                lecturer_results = cursor.fetchall()

                # Execute the student's query
                cursor.execute(student_query)
                student_results = cursor.fetchall()

                # Compare the results
                if lecturer_results == student_results:
                    # Execute the EXPLAIN QUERY PLAN for both queries
                    cursor.execute('EXPLAIN QUERY PLAN ' + student_query)
                    student_explain = cursor.fetchall()

                    cursor.execute('EXPLAIN QUERY PLAN SELECT * FROM lecturer_solution')
                    lecturer_explain = cursor.fetchall()

                    # Compare the EXPLAIN QUERY PLAN output
                    if self.compare_query_plan(lecturer_explain, student_explain):
                        # Compare additional factors for optimization and efficiency
                        student_stats = self.get_query_stats(cursor, student_query)
                        lecturer_stats = self.get_query_stats(cursor, 'SELECT * FROM lecturer_solution')

                        # Compare number of rows processed
                        if student_stats['Rows'] == lecturer_stats['Rows']:
                            # Compare number of indexes used
                            if student_stats['Index'] == lecturer_stats['Index']:
                                # Check for potential performance issues (e.g., full table scans)
                                if 'SCAN TABLE' not in student_explain and 'SCAN TABLE' not in lecturer_explain:
                                    return 100  # Full score for correct results, similar execution plan, and optimized query
                                else:
                                    return 80  # Partial score for correct results, similar execution plan, but potential performance issue
                            else:
                                return 70  # Partial score for correct results but different indexes used
                        else:
                            return 60  # Partial score for correct results but different number of rows processed
                    else:
                        return 50  # Partial score for different execution plan

                else:
                    return 0  # Zero score for incorrect results

        except sqlite3.DatabaseError as e:
            print(f"Database Error: {e}")

        return 0  # Zero score for any other errors

    def compare_query_plan(self, plan1, plan2):
        """
        Compare two SQLite query plans.

        Parameters:
        - plan1 (list): List of dictionaries representing the first query plan.
        - plan2 (list): List of dictionaries representing the second query plan.

        Returns:
        - bool: True if the plans are similar, False otherwise.
        """
        # Implement your logic for comparing query plans
        # This could involve parsing and comparing specific attributes
        # Adjust based on the actual structure of the plans

        # Placeholder: Assuming the plans are lists of dictionaries
        if len(plan1) != len(plan2):
            return False

        for step1, step2 in zip(plan1, plan2):
            # Custom comparison logic based on attributes
            if step1.get('operation') != step2.get('operation'):
                return False
            # Add more comparisons based on your specific needs

        return True

    def get_query_stats(self, cursor, query):
        """
        Retrieve and parse query execution statistics.

        Parameters:
        - cursor: SQLite cursor object.
        - query (str): SQL query for which statistics are to be retrieved.

        Returns:
        - dict: Dictionary containing query execution statistics.
        """
        try:
            cursor.execute('ANALYZE ' + query)
            stats_result = cursor.fetchall()

            # Assuming stats_result is a list of dictionaries
            stats = {}
            for row in stats_result:
                stats[row['Metric']] = row['Value']

            return stats

        except sqlite3.DatabaseError as e:
            print(f"Database Error in get_query_stats: {e}")
            return {}

    def close_connection(self):
        """
        Close the SQLite database connection.
        """
        self.connection.close()

