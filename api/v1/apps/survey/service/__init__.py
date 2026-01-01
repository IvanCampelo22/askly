# @async_session
# async def update(session: AsyncSession, survey_id: int, questions_data: List[dict], **kwargs) -> Any:
#     """Atualiza formulários e cria uma nova versão com perguntas do tipo Scale"""

#     # Recuperar o survey existente
#     result_survey = await session.execute(select(Survey).where(Survey.id == survey_id))
#     existing_survey = result_survey.scalars().first()

#     if not existing_survey:
#         raise ValueError("Formulário não encontrado ou já foi respondido")

#     # Recuperar todas as perguntas do tipo Scale associadas ao survey
#     result_scale = await session.execute(select(Scale).where(Scale.survey_id == survey_id))
#     existing_scales = result_scale.scalars().all()

#     # Criar nova versão do survey
#     new_survey = Survey(
#         version=existing_survey.version + 1,
#         **{key: kwargs.get(key, getattr(existing_survey, key)) for key in kwargs}
#     )
#     session.add(new_survey)
#     await session.flush()  # flush para obter o id da nova versão

#     # Adicionar novas versões das perguntas do tipo Scale
#     for existing_scale in existing_scales:
#         new_scale_data = next((s for s in questions_data if s.get('id') == existing_scale.id), {})
        
#         new_scale = Scale(
#             survey_id=new_survey.id,
#             order=new_scale_data.get('order', existing_scale.order),
#             type=new_scale_data.get('type', existing_scale.type),
#             input_type=new_scale_data.get('input_type', existing_scale.input_type),
#             text=new_scale_data.get('text', existing_scale.text),
#             scale_min=new_scale_data.get('scale_min', existing_scale.scale_min),
#             scale_max=new_scale_data.get('scale_max', existing_scale.scale_max),
#         )
#         session.add(new_scale)

#     # Excluir a versão antiga das perguntas Scale
#     for scale in existing_scales:
#         await session.delete(scale)

#     # Excluir o survey antigo
#     await session.delete(existing_survey)
#     await session.commit()

#     return new_survey


# @async_session
# async def update(session: AsyncSession, survey_id: int, questions_data: List[dict], **kwargs) -> Any:
#     """Atualiza formulários"""

#     question_type = questions_data.get("type")

#     result_survey = await session.execute(select(Survey).where(Survey.id == survey_id))
#     existing_survey = result_survey.scalars().first()
    
#     if not existing_survey:
#         raise ValueError("Formulário não encontrado ou já foi respondido")

#     result_scale = await session.execute(select(Scale).where(Scale.survey_id == survey_id))
#     existing_scales = result_scale.scalars().all()

#     result_text = await session.execute(select(Text).where(Text.survey_id == survey_id))
#     existing_text = result_text.scalars().all()

#     result_email = await session.execute(select(Email).where(Email.survey_id == survey_id))
#     existing_email = result_email.scalars().all()

#     result_document = await session.execute(select(Document).where(Document.survey_id == survey_id))
#     existing_document = result_document.scalars().all()

#     result_multiple_choice = await session.execute(select(MultipleChoice).where(MultipleChoice.survey_id == survey_id))
#     existing_multiple_choice = result_multiple_choice.scalars().all()

#     result_single_choice = await session.execute(select(SingleChoice).where(SingleChoice.survey_id == survey_id))
#     existing_single_choice = result_single_choice.scalars().all()

#     new_survey = Survey(
#         id=None,
#         version=existing_survey.version + 1,
#         **{key: kwargs.get(key, getattr(existing_survey, key)) for key in kwargs}
#     )
    
#     session.add(new_survey)
#     await session.flush() 

#     if question_type == "nps":
#         await new_scale_for_update(session=session, existing_scales=existing_scales, update_scale=questions_data, new_survey=new_survey)    
#         await session.commit()
        
#     elif question_type == "text":
#         await new_text_for_update(session=session, existing_text=existing_text, update_text=questions_data, new_survey=new_survey)

#     elif question_type == "email":
#         await new_email_for_update(session=session, existing_email=existing_email, update_email=questions_data, new_survey=new_survey)
    
#     elif question_type == "document":
#         await new_document_for_update(session=session, existing_document=existing_document, update_document=questions_data, new_survey=new_survey)

#     elif question_type == "multiple_choice":
#         await new_multiple_choice_for_update(session=session, existing_multiple_choice=existing_multiple_choice, update_multiple_choice=questions_data, new_survey=new_survey)

#     elif question_type == "single_choice":
#         await new_single_choice_for_update(session=session, existing_single_choice=existing_single_choice, update_single_choice=questions_data, new_survey=new_survey)

#     await session.delete(existing_survey)
#     await session.commit()

#     return new_survey