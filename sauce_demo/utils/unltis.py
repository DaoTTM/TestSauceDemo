
import requests
from sauce_demo.utils.config import BASE_URL, USERNAME, PASSWORD, PROJECT_ID, RUN_ID

def get_all_test_cases():
    url= f"{BASE_URL}index.php?/api/v2/get_cases/{PROJECT_ID}"
    response = requests.get(url, auth=(USERNAME, PASSWORD))

    if response.status_code !=200:
        print(f"Lỗi khi lấy test case: {response.json()}")
        return {}


    cases=response.json()["cases"]
    return {case["title"]:case["id"] for case in cases}

def update_test_result(test_name, status_id, comment=""):
    test_cases = get_all_test_cases()
    test_case_id = test_cases.get(test_name)

    if test_case_id is None:
        print(f"Khong tim thay Test Case Id cho '{test_name}'")
        return False

    url=f"{BASE_URL}index.php?/api/v2/add_result_for_case/{RUN_ID}/{test_case_id}"
    data ={"status_id":status_id,"comment":comment}
    response =requests.post(url, json=data, auth=(USERNAME, PASSWORD))

    if response.status_code == 200:
        print(f"Cap nat TestRail thanh cong cho {test_name}")
        return True
    else:
        print(f"Loi cap nhat TestRail:{response.json()}")
        return False
