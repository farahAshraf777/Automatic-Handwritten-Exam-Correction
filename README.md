# ScanScore
Developed an automated grading system for handwritten exams, leveraging OCR and AI technologies to streamline the evaluation process. The system features secure user authentication, AI-driven grading, and comprehensive exam management tools for both teachers and students.

## Features

User Authentication and Authorization: Secure login credentials for both teachers and students, with appropriate permissions and access controls for each role.

Document Upload: Teachers can upload scanned exam papers containing students' answers for processing. Teachers can choose the OCR model when uploading papers:

Model-1: Recognizes characters and uses AI to correct possible spelling mistakes.
Model-2: Recognizes characters as they are written by students.
OCR Processing: Automated Optical Character Recognition (OCR) processing of uploaded papers to extract written content, including student answers and IDs.

Automatic Correction: AI-driven grading using SBERT (Sentence-BERT) with cosine similarity. SBERT encodes answers into embeddings for semantic comparison, evaluating and grading student answers against model responses. The system also uses keywords provided by teachers to refine grading accuracy by checking for specific terms in student answers.

Exam Management: Teachers can submit exam questions, model answers, and keywords. The system allows AI-generated model answers, which teachers can accept, edit, or refine with additional constraints.

Exam Publishing: Teachers can set exams as active (published) or inactive. Active exams are available for students to take online, while inactive exams are in preparation or grading stages.

Student Submissions: Students can submit answers for active exams online, and teachers can view these submissions once the exam is finished.

Grading and Modifications: Post-AI grading allows teachers to review, fine-tune, and manually adjust final grades before approval. Teachers can increase all grades of a specific exam by a certain value or round grades up to the nearest integer.

Student Interface: Students can log in to view their profile, participate in active exams, and view their past exam grades along with the model answers.

Data Management: Secure storage and retrieval of all exam-related data, including questions, model answers, student submissions, grades, and any modifications made by teachers.

Exam Export Grades: Teachers can export grades to an Excel sheet after OCR processing and AI grading, allowing for record-keeping and analysis.



## Contributing


## License

