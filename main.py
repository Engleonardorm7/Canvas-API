import requests


def read(group,class_guide):
    group=group
    class_guide=class_guide
    
    url_activity = f"https://virtualmbs.instructure.com/api/v1/courses/{group}/assignments/{class_guide}/submissions"
    url_students=f"https://virtualmbs.instructure.com/api/v1/courses/{group}/students"
    # https://virtualmbs.instructure.com/api/v1/courses/1348/groups/IDGROUP/users?enrollment_type=student
    headers = {
        "Authorization": "Put your canvas key here"
    }
    response_students = requests.get(url_students, headers=headers, verify=True)

    if response_students.status_code == 200:
        students=response_students.json()
        for student in students:
            student_name = student["name"]
            user_id = student["id"]
            url_activity = f"https://virtualmbs.instructure.com/api/v1/courses/{group}/assignments/{class_guide}/submissions/{user_id}"
            response = requests.get(url_activity, headers=headers, verify=True)
        
            # Verificar si se pudo obtener la nota de la actividad correctamente
            if response.status_code == 200:
                grade_info  = response.json()["score"]
            
                print(f'{student["id"]}- Nombre del estudiante: {student_name}, Nota de la actividad {class_guide}: {grade_info}')
            else:
                print("Error en la solicitud de la nota de la actividad {class_guide} del estudiante {}. Código de estado: {}".format(student["name"], response.status_code))

            
    else:
        print("Error en la solicitud de la lista de estudiantes. Código de estado:", response_students.status_code)



def post(user_id,grade,group,class_guide):



    
    class_guide=class_guide
    group=group
    user_id = user_id
    new_grade=grade

    url_student_activity = f"https://virtualmbs.instructure.com/api/v1/courses/{group}/assignments/{class_guide}/submissions/{user_id}"
    
    url_students=f"https://virtualmbs.instructure.com/api/v1/courses/{group}/students"

    headers = {
        "Authorization": "Put your canvas key here"
    }
    response_students = requests.get(url_students, headers=headers,verify=True)

    if response_students.status_code == 200:
        students = response_students.json()
        
        for student in students:
            student_name=student["name"]
            if student["id"] == user_id:
                data = {
                            "submission": {
                                "posted_grade": new_grade
                            }
                        }
                response = requests.put(url_student_activity, headers=headers, json=data, verify=True)
                if response.status_code == 200:
                    print(f"Nota actualizada correctamente para el estudiante {student_name}")
                else:
                    print(f"Error en la actualización de la nota para el estudiante {student_name}. Código de estado: {response.status_code}")
                break
        else:
            print(f"No se encontró el estudiante {student_name} en la lista.")
    else:
        print(f"Error en la solicitud de la lista de estudiantes. Código de estado: {response_students.status_code}")

# post(213,2)
# read()