
### Student Management System

   This is a Django-based Student Management System that allows you to manage student information including their first name, last name, email, date of birth, enrollment date, and grade.

   ## Setup

   ### Prerequisites

   - Python 3.x
   - pip
   - virtualenv

   ### Installation

   1. **Clone the repository:**

      ```sh
      git clone https://github.com/ivanivan999/student_management.git
      cd student_management
      ```

   2. **Set up a virtual environment:**

      ```sh
      python3 -m venv venv
      source venv/bin/activate
      ```

   3. **Install the required packages:**

      ```sh
      pip install -r requirements.txt
      ```

   4. **Set Up Environment Variables**:

   -   Copy the example environment file:
      
        ```sh
        cp .env.example .env
        ```

   -   Edit the `.env` file to include your secret key and other settings:

         ```sh
        SECRET_KEY=your_secret_key

        DEBUG=True

        ALLOWED_HOSTS=127.0.0.1,localhost
        ```

   5. **Apply migrations:**

      ```sh
      python manage.py migrate
      ```

   ## Running the Project

   6. **Start the development server:**

      ```sh
      python manage.py runserver
      ```

   7. Open your web browser and go to \`http://127.0.0.1:8000/\`.


   ## License

   This project is licensed under the MIT License.
 