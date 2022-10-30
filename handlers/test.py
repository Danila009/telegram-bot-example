from aiogram import types
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext

from keyboards import test_question

from states.test import Test


async def enter_test(message: types.Message):
    await message.answer('Question', reply_markup=test_question.menu_yes_no)

    await Test.Q1.set()


async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(answer1=answer)

    if answer == 'next':
        await message.answer('kotlin or java ?', reply_markup=test_question.menu_java_kotlin)
        await Test.next()
    elif answer == 'exit':
        await message.answer('exit test', reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
    else:
        await message.answer('Question', reply_markup=test_question.menu_yes_no)


async def answer_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()

    answer1 = data.get('answer1')
    answer2 = message.text

    print(answer1)

    if answer2 == 'kotlin':
        await message.answer('Kotlin — статически типизированный, объектно-ориентированный язык программирования, '
                             'работающий поверх Java Virtual Machine и разрабатываемый компанией JetBrains. Также '
                             'компилируется в JavaScript и в исполняемый код ряда платформ через инфраструктуру LLVM.')
        await message.answer('finish', reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
    elif answer2 == 'java':
        await message.answer('Java — строго типизированный объектно-ориентированный язык программирования общего '
                             'назначения, разработанный компанией Sun Microsystems. Разработка ведётся сообществом, '
                             'организованным через Java Community Process; язык и основные реализующие его технологии '
                             'распространяются по лицензии GPL.')
        await message.answer('finish', reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
    else:
        await message.answer('kotlin or java ?', reply_markup=test_question.menu_java_kotlin)


def register_test(dp: Dispatcher):
    dp.register_message_handler(enter_test, commands=['test'], state=None)
    dp.register_message_handler(answer_q1, state=Test.Q1)
    dp.register_message_handler(answer_q2, state=Test.Q2)
