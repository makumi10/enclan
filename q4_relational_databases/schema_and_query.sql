-- Question 4: students, courses, and enrollments

CREATE TABLE students (
    student_id   INTEGER PRIMARY KEY AUTO_INCREMENT,
    first_name   VARCHAR(100) NOT NULL,
    last_name    VARCHAR(100) NOT NULL,
    email        VARCHAR(255) UNIQUE NOT NULL,
    date_of_birth DATE
);

CREATE TABLE courses (
    course_id    INTEGER PRIMARY KEY AUTO_INCREMENT,
    course_name  VARCHAR(255) NOT NULL,
    description  TEXT,
    credits      INTEGER
);

-- links students to courses (a student can take many courses, a course can have many students)
CREATE TABLE enrollments (
    enrollment_id   INTEGER PRIMARY KEY AUTO_INCREMENT,
    student_id      INTEGER NOT NULL,
    course_id       INTEGER NOT NULL,
    enrollment_date DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    UNIQUE (student_id, course_id) -- stops the same student being enrolled in a course twice
);

-- students enrolled in "Introduction to Programming"
SELECT s.student_id, s.first_name, s.last_name, s.email
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id
WHERE c.course_name = 'Introduction to Programming';
