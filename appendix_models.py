from datetime import date

from pydantic import BaseModel

'''Получение в течение не менее 2-х следующих друг за другом промежуточных аттестаций, предшествующих назначению
повышенной государственной академической стипендии, только оценок «отлично»'''


class ExcellentStudent(BaseModel):
    id: int = None
    id_application: int
    id_person: str = None
    excellent: bool


'''Получатель награды (приза) в течение 1-ого года, предшествующего назначению повышенной государственной академической
стипендии, за результаты проектной деятельности и (или) опытно-конструкторской работы'''


class ArticleWriter(BaseModel):
    id: int = None
    id_application: int
    id_person: str = None
    event_name: str
    prize_place: int
    participation: str
    date: date
    scores: float = 0.0


'''Победитель или призер международной, всероссийской, ведомственной или региональной олимпиады, конкурса, соревнования,
состязания или иного мероприятия, направленных на выявление учебных достижений студентов, проведенных в течение 1-ого года,
предшествующего назначению повышенной государственной академической:'''


class OlympiadWinner(BaseModel):
    id: int = None
    id_application: int
    id_person: str = None
    event_name: str
    level: str
    prize_place: int
    participation: str
    date: date
    scores: float = 0.0


__all__ = ["ArticleWriter", "ExcellentStudent", "OlympiadWinner"]