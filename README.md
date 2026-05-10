# Difficulty-Adjustment-Logic
 Difficulty Adjustment Logic System that predicts the next question difficulty level based on previous user scores. I developed the backend logic using Python and Flask, created the frontend interface using HTML and CSS, and integrated both components to ensure smooth functionality.

#This project was developed using Python Flask for backend processing and HTML/CSS for frontend design.

# Features
- Dynamic difficulty prediction
- Adaptive evaluation system
- Frontend and backend integration
- REST API support
- Simulation testing
- Edge case handling

# Technologies Used
- Python
- Flask
- HTML
- CSS
- NumPy
- Visual Studio Code

# Project Structure
task-1/
│
├── difficulty_app.py
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css

# Installation

step-1:Clone Repository
```bash
git clone <repository-link>

Step 2: Navigate to Project Folder
cd difficulty_project

Step 3: Install Required Libraries
pip install flask numpy

Running the Project
Run the following command:python app.py
Open browser:http://127.0.0.1:5000

````markdown id="vg8hcc"
# API Details

## Endpoint
```text
/predict
````

## Method

```text id="0oz62n"
POST
```

## Sample Input

```json
{
  "scores": [85, 80, 95]
}
```

## Sample Output

```json id="r7v7k4"
{
  "next_difficulty": "hard"
}
```

# Decision Logic
| Average Score | Difficulty |
| ------------- | ---------- |
| Below 35      | Easy       |
| 35 – 75       | Medium     |
| Above 75      | Hard       |

# Edge Cases Handled
* Consistent low scores
* Consistent high scores
* Minimum question count
* Oscillation prevention

# Simulation Test Cases

| Scores       | Predicted Difficulty |
| ------------ | -------------------- |
| [25, 30, 35] | Easy                 |
| [50, 65, 60] | Medium               |
| [85, 80, 95] | Hard                 |
| [72, 73, 74] | Medium               |
| [15, 10, 20] | Medium               |

# Results
The system successfully predicts the next difficulty level based on previous user scores and dynamically adapts question difficulty.

# Future Enhancements
* Machine Learning integration
* Real-time analytics
* Database connectivity
* User authentication
* Advanced adaptive learning

# Conclusion

The Difficulty Adjustment Logic System provides a simple and effective adaptive evaluation mechanism that dynamically adjusts question difficulty and ensures fair assessment.



