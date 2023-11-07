import requests

base_url = "https://byui.instructure.com/"
course_endpoint = "api/v1/courses"
token = "10706~uWoI3hfmV1nQqmWtEX0XaQJXD6nN8DYkeKOvFVCmwEI8eVurY9tHf1CroxCE4btq"

headers = {
    "Authorization": f"Bearer {token}"
}

course_url = f"{base_url}{course_endpoint}?enrollment_state=active"

course_response = requests.get(course_url, headers=headers)

if course_response.status_code == 200:
    courses = course_response.json()
    
    for course in courses:
        course_id = course["id"]
        course_name = course["name"]
        course_code = course["course_code"]
        
        print(f"{course_code} - {course_name}")

        assignment_endpoint = f"api/v1/courses/{course_id}/assignments"
        assignment_url = f"{base_url}{assignment_endpoint}"

        assignment_response = requests.get(assignment_url, headers=headers)

        if assignment_response.status_code == 200:
            assignments = assignment_response.json()

            for assignment in assignments:
                assignment_name = assignment["name"]
                due_date = assignment["due_at"]

                print(f"{assignment_name} - {due_date}")

        else:
            print(f"API request failed. Error code {assignment_response.status_code}")

else:
    print(f"API request failed. Error code {course_response.status_code}")