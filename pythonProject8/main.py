from flask import Flask

from utils import load_candidates, format_candidates, load_candidate_by_id, load_candidate_by_skill

app = Flask(__name__)

''' создание 3-х контроллеров - главная страница - вывод кандидата по 3-м описаниям"""
 """ под страница candidates - выводит описания в зависимости от номера идентификации
  """ под страница навыки, выводит описание кандидата в зависимости от навыка'''


@app.route("/")
def main_page():
    candidates_list = load_candidates('candidates.json')

    return format_candidates(candidates_list)


@app.route("/candidates/<int:candidate_id>")
def candidate_page(candidate_id):
    candidates_list = load_candidates("candidates.json")

    candidate = load_candidate_by_id(candidates_list, candidate_id)

    result = f"<img src={candidate['picture']}>"
    return result + format_candidates([candidate])


@app.route("/skills/<skill>")
def have_skills(skill):
    candidates_list = load_candidates('candidates.json')

    return format_candidates(load_candidate_by_skill(candidates_list, skill))


app.run()
