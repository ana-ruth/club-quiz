import mysql.connector
from .schemas import QuizResponse
from mysql.connector import Error
import mysql.connector
from mysql.connector import Error
from .schemas import QuizResponse

class Database:
    @staticmethod
    def connect_to_database():
        try:
            db = mysql.connector.connect(
                host="sql5.freesqldatabase.com",
                user="sql5734190",
                password="XETbGHKPuj",
                database="sql5734190"
            )
            print("Successfully connected to the database.")
            return db
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    @staticmethod
    def insert_student_data(db, quiz_data: QuizResponse):
        cursor = db.cursor()
        query = """
        INSERT INTO student_responses 
        (student_id, extracurricular_interest, communityService, genderSpecific, free_time_preference, cultureFocused, personal_goals) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        # Generate a unique student_id (you might want to use a more robust method)
        cursor.execute("SELECT MAX(student_id) FROM student_responses")
        max_id = cursor.fetchone()[0]
        student_id = (max_id or 0) + 1

        values = (
            student_id,
            quiz_data.extracurricular,
            int(quiz_data.volunteering),
            int(quiz_data.gender),
            quiz_data.extracurricular,  # Using extracurricular for free_time_preference
            int(quiz_data.ethnicity),
            quiz_data.field  # Using field for personal_goals
        )
        cursor.execute(query, values)
        db.commit()
        print("Student data inserted successfully.")
        return student_id

    @staticmethod
    def get_top_3_clubs(db, student_id):
        try:
            cursor = db.cursor()
            query = """
            SELECT c.club_name
            FROM clubs c
            JOIN student_responses sr ON sr.student_id = %s
            ORDER BY (CASE WHEN c.field_of_interest = sr.extracurricular_interest THEN 1 ELSE 0 END +
                    CASE WHEN c.community_service = sr.communityService THEN 1 ELSE 0 END +
                    CASE WHEN c.gender_specific = sr.genderSpecific THEN 1 ELSE 0 END +
                    CASE WHEN c.culture_focus = sr.cultureFocused THEN 1 ELSE 0 END) DESC
            LIMIT 3;
            """
            cursor.execute(query, (student_id,))
            results = cursor.fetchall()
            top_clubs = [row[0] for row in results]
            cursor.close()
            return top_clubs
        except Error as e:
            print(f"Error fetching top clubs: {e}")
            return []  # Return an empty list in case of an error

    @staticmethod
    def handle_student_submission(db, quiz_data: QuizResponse):
        try:
            student_id = Database.insert_student_data(db, quiz_data)
            top_clubs = Database.get_top_3_clubs(db, student_id)
            
            if top_clubs:
                print(f"Found {len(top_clubs)} top clubs: {top_clubs}")
            else:
                print("No top clubs found.")
                
                return top_clubs if top_clubs else []
        except Error as e:
            print(f"Error handling student submission: {e}")
            return []

    @staticmethod
    def close_database_connection(db):
        if db:
            db.close()
    