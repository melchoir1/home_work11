import json


def load_candidates_from_json():
    """возвращает список всех кандидатов"""
    with open("candidates.json", 'r', encoding='utf-8') as file:
        return json.load(file)
#print(load_candidates_from_json())

def get_candidate(candidate_id):
    """возвращает одного кандидата по его id"""
    for candidate in load_candidates_from_json():
        if candidate['id'] == candidate_id:
            return candidate
#print(get_candidate(1))

def get_candidates_by_name(candidate_name):
    """возвращает кандидатов по имени"""
    list_result = []
    for candidate in load_candidates_from_json():
        if candidate['name'] == candidate_name:
            list_result.append(candidate)
    return list_result
#print(get_candidates_by_name("Adela Hendricks"))

def get_candidates_by_skill(skill_name):
    """возвращает кандидатов по навыку"""
    list_result = []
    for candidate in load_candidates_from_json():
        if skill_name in candidate["skills"].lower().split(', '):
            list_result.append(candidate)
    return list_result
#print(get_candidates_by_skill('python'))

