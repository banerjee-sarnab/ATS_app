# ATS (Applicant Tracking System) Web Application

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Overview

This web application is an Applicant Tracking System (ATS) built with Flask. It allows users to upload resumes (in PDF format) and job descriptions, and it calculates the similarity score between them using Natural Language Processing (NLP) techniques especially text-similarity. The project is designed to streamline the hiring process by automatically matching candidates to job openings.

## Features

- Upload and process candidate resumes (PDF format).
- Upload job descriptions.
- Calculate and display similarity scores between resumes and job descriptions.
- User-friendly web interface.
- Interactive feedback to users based on similarity scores.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.0 or higher installed.
- Git installed (for version control).

### Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/banerjee-sarnab/ATS_app.git
   cd ATS_app

2. Install the project dependencies:
   
   ```shell
   pip install -r requirements.txt

### Usage
Start the Flask application:

```shell
flask run
```

Open your web browser and navigate to http://localhost:5000 to access the ATS web application.
Upload candidate resumes in PDF format and job descriptions to calculate similarity scores.

### License
This project is licensed under the MIT License. See the LICENSE file for details.
