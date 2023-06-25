from fastapi import APIRouter

from eco_challenge.auth.dependencies import CurrentAdmin
from eco_challenge.core.storages.quiz_storage import QuizStorageDepends
from eco_challenge.quiz_app.models.quiz_model import QuizGet, QuizCreate, QuizValidateAction, QuizValidationResponse

router = APIRouter(prefix='/quiz', tags=['Quiz'])


@router.post('/')
async def create_quiz(quiz_create: QuizCreate, storage: QuizStorageDepends, _: CurrentAdmin) -> QuizGet:
    return await storage.save_object(quiz_create)


@router.post('/validate')
async def validate(
    validation_action: QuizValidateAction,
    storage: QuizStorageDepends,
    _: CurrentAdmin
) -> QuizValidationResponse:
    quiz = await storage.get_obj(validation_action.quiz_id)
    answers = {}
    for question in quiz.questions:
        for answer in question.answers:
            if answer.answer_id == validation_action.answers[question.question_id]:
                answers[question.question_id] = answer.is_correct
                break
    return QuizValidationResponse(quiz_id=quiz.quiz_id, answers=answers)


@router.get('/')
async def get_quizzes(storage: QuizStorageDepends) -> list[QuizGet]:
    return await storage.get_objects()


@router.get('/{quiz_id}')
async def get_quiz(quiz_id: int, storage: QuizStorageDepends):
    return await storage.get_obj(quiz_id)


@router.delete('/{quiz_id}')
async def delete_quiz(quiz_id: int, storage: QuizStorageDepends, _: CurrentAdmin):
    return await storage.delete_object(quiz_id)
