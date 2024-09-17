# Backend Candidate Team Challenge

## Project Overview

You are tasked with creating a Candidate Grading System using FastAPI. This system will allow recruiters to manage projects, candidates, and implement a team-matching algorithm. Your submission must include the final application implemented with this boilerplate, or using your own FastAPI setup.

## Part 1: FastAPI Application

### Requirements
1. Implement the following database models and schemas:
   - Project
   - Candidate

2. Implement the following endpoints:
   - CRUD operations for projects and candidates
   - Basic input validation and error handling with Pydantic
   - Unit tests for your API endpoints
   - An endpoint to create ideal teams for candidates (discussed in Part 2)

3. Implement proper logging and error handling throughout the application 

### Sample JSON Structures

#### Project:
```json
{
  "title": "Full-stack Project",
  "skills": [
    {"name": "Python", "expertise_level": 7},
    {"name": "JavaScript", "expertise_level": 8},
    {"name": "React", "expertise_level": 6},
    {"name": "SQL", "expertise_level": 5},
    {"name": "DevOps", "expertise_level": 4}
  ]
}
```

#### Candidate:
```json
{
  "name": "Alice",
  "skills": [
    {"name": "Python", "expertise_level": 9},
    {"name": "JavaScript", "expertise_level": 7},
    {"name": "React", "expertise_level": 8}
  ]
}
```

### Brownie Points

You are not required to complete these tasks, but they will be considered as bonus points:

- Implement proper formatting and linting using tools like Black/ruff/Flake8/etc.
- Add authentication for users
- Add custom logger configuration
- Implement pagination for list endpoints
- Add sorting and filtering options for list endpoints
- Add GitHub CI actions to automate testing/linting of your code

## Part 2: Optimal Team Algorithm

Implement an algorithm to form the best possible team for a project based on required skills and candidate expertise levels.

### Requirements:

1. Implement a function that takes project details, a list of candidates, and a team size, and returns the optimal team.
2. The team should cover all required skills with the highest possible expertise while minimizing overlap.
3. If multiple teams can cover all skills, prefer the team with the highest average expertise across all required skills.
4. If not all skills can be covered, the team should maximize the coverage and expertise of the skills it can cover.

### Constraints:

- 1 <= team_size <= 10
- 1 <= number of required skills <= 20
- 1 <= number of candidates <= 100

### Evaluation Criteria:

- Correctness: The algorithm should always produce a valid team that respects the given constraints.
- Optimality: The team formed should be optimal or near-optimal in terms of skill coverage and expertise.
- Efficiency: The algorithm should be able to handle the maximum constraints in a reasonable time (e.g., under 5 seconds).

## Example Inputs and Outputs

### Example 1:

POST `/api/form-team/`

Request Body:
```json
{
  "project_id": 1,
  "candidate_ids": [1, 2, 3, 4],
  "team_size": 3
}
```

Here are the details of the project and candidates:

#### Project:
```json
{
  "id": 1,
  "title": "Full-stack Project",
  "skills": [
    {"name": "Python", "expertise_level": 7},
    {"name": "JavaScript", "expertise_level": 8},
    {"name": "React", "expertise_level": 6},
    {"name": "SQL", "expertise_level": 5},
    {"name": "DevOps", "expertise_level": 4}
  ]
}
```

#### Candidates:
```json
{
  "candidates": [
    {
      "id": 1,
      "name": "Alice",
      "skills": [
        {"name": "Python", "expertise_level": 9},
        {"name": "JavaScript", "expertise_level": 7},
        {"name": "React", "expertise_level": 8}
      ]
    },
    {
      "id": 2,
      "name": "Bob",
      "skills": [
        {"name": "JavaScript", "expertise_level": 9},
        {"name": "React", "expertise_level": 8},
        {"name": "SQL", "expertise_level": 7}
      ]
    },
    {
      "id": 3,
      "name": "Charlie",
      "skills": [
        {"name": "Python", "expertise_level": 8},
        {"name": "SQL", "expertise_level": 8},
        {"name": "DevOps", "expertise_level": 7}
      ]
    },
    {
      "id": 4,
      "name": "Diana",
      "skills": [
        {"name": "JavaScript", "expertise_level": 8},
        {"name": "React", "expertise_level": 7},
        {"name": "DevOps", "expertise_level": 6}
      ]
    }
  ]
}
```

#### Expected Response:
```json
{
  "team": [
    {
      "candidate_id": 1,
      "name": "Alice",
      "assigned_skills": ["Python", "React"]
    },
    {
      "candidate_id": 2,
      "name": "Bob",
      "assigned_skills": ["JavaScript", "SQL"]
    },
    {
      "candidate_id": 3,
      "name": "Charlie",
      "assigned_skills": ["DevOps"]
    }
  ],
  "total_expertise": 41,
  "coverage": 1.0
}
```

### Example 2:

POST `/api/form-team/`

Request Body:
```json
{
  "project_id": 2,
  "candidate_ids": [1, 2, 3, 4],
  "team_size": 2
}
```

Here are the details of the project and candidates:

#### Project:
```json
{
  "id": 2,
  "title": "Machine Learning Research Project",
  "skills": [
    {"name": "Python", "expertise_level": 8},
    {"name": "Machine Learning", "expertise_level": 9},
    {"name": "Data Analysis", "expertise_level": 7},
    {"name": "Statistics", "expertise_level": 6},
    {"name": "Deep Learning", "expertise_level": 5}
  ]
}
```

#### Candidates:
```json
{
  "candidates": [
    {
      "id": 1,
      "name": "Alice",
      "skills": [
        {"name": "Python", "expertise_level": 9},
        {"name": "Machine Learning", "expertise_level": 8},
        {"name": "Data Analysis", "expertise_level": 7}
      ]
    },
    {
      "id": 2,
      "name": "Bob",
      "skills": [
        {"name": "Python", "expertise_level": 7},
        {"name": "Statistics", "expertise_level": 8},
        {"name": "Deep Learning", "expertise_level": 6}
      ]
    },
    {
      "id": 3,
      "name": "Charlie",
      "skills": [
        {"name": "Machine Learning", "expertise_level": 9},
        {"name": "Deep Learning", "expertise_level": 8}
      ]
    },
    {
      "id": 4,
      "name": "Diana",
      "skills": [
        {"name": "Python", "expertise_level": 8},
        {"name": "Data Analysis", "expertise_level": 9},
        {"name": "Statistics", "expertise_level": 7}
      ]
    }
  ]
}
```

Expected Response:
```json
{
  "team": [
    {
      "candidate_id": 1,
      "name": "Alice",
      "assigned_skills": ["Python", "Machine Learning", "Data Analysis"]
    },
    {
      "candidate_id": 2,
      "name": "Bob",
      "assigned_skills": ["Statistics", "Deep Learning"]
    }
  ],
  "total_expertise": 38,
  "coverage": 1.0
}
```

## Part 3: Implement Scoring in Candidate Model

You've been provided an endpoint that provides candidates a special score based on their skills. Your job is to add this special score to the Candidate schema. The code for this mock server is available in: [`takehome/mock.py`](https://github.com/SimplifyJobs/backend-take-home/blob/master/takehome/mock.py)

1. This API is flaky as it is powered by an ML model that is not always available. You must gracefully handle retries until you get a score.
2. Given that the API may take time to respond, you may want to parallelize requests to this API and cache results somewhere.
3. Add this score to the Read endpoint for the candidate as well as the results to Part 2's Team Formation API.

## Evaluation Criteria

Your solution will be evaluated based on the following criteria:

1. Correctness and efficiency of the team formation algorithm
2. Code quality, organization, and adherence to PEP 8 style guidelines
3. Proper use of FastAPI features and best practices
4. Appropriate use of Pydantic for data validation and serialization
5. Integration of the algorithm with the FastAPI application
6. Error handling and input validation
7. Quality of unit tests
8. Clarity of explanation in comments and README
9. Bonus features implemented

## Submission Guidelines

1. Fork this repository or create a new repository with your solution. Your solution must be a FastAPI application that can run with the same application name provided in the boilerplate.
2. Include a SUBMISSION.md file with:
   - Brief explanation of your algorithm and its time complexity
   - Any assumptions you made
   - List of completed features and any known issues
   - Any special instructions for running the application
3. Ensure your code is well-commented
4. Submit the link to your GitHub repository

Good luck! We look forward to reviewing your solution.
