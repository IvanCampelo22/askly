from api.v1.apps.questions.models.models import Text, MultipleChoice, SingleChoice, Email, Document, Scale, MultiQuestionMulti, MultiQuestionSingle


async def new_scale_for_update(session, existing_scales, questions_data, new_survey) -> None:
    """
    Add a new record with the updated data, and delete the previous record specifically for the Scale question type
    
    Args:
        session (sqlalchemy.ext.asyncio.AsyncSession): The SQLAlchemy session object.
        existing_scales (Any): The model class representing the question Scale
        questions_data (Any): The json data that comes from the update request
        new_survey (Any): The updated form data, which was added and deleted, along with the question

    Raises:
        TypeError: If `existing_scales` is not an instance of a supported class.
    
    """

    if not isinstance(existing_scales, (Scale)):
        raise TypeError("new_scale_for_update only works with Scale instances")

    for existing_scale in existing_scales:
        new_scale_data = next((s for s in questions_data if s.get('id') == existing_scale.id), {})
        
        new_scale = Scale(
            survey_id=new_survey.id,
            order=new_scale_data.get('order', existing_scale.order),
            type=new_scale_data.get('type', existing_scale.type),
            input_type=new_scale_data.get('input_type', existing_scale.input_type),
            text=new_scale_data.get('text', existing_scale.text),
            scale_min=new_scale_data.get('scale_min', existing_scale.scale_min),
            scale_max=new_scale_data.get('scale_max', existing_scale.scale_max),
        )
        session.add(new_scale)

    for scale in existing_scales:
        await session.delete(scale)


async def new_text_for_update(session, existing_texts, questions_data, new_survey) -> None:
    """
    Add a new record with the updated data, and delete the previous record specifically for the Text question type
    
    Args:
        session (sqlalchemy.ext.asyncio.AsyncSession): The SQLAlchemy session object.
        existing_texts (Any): The model class representing the question Text
        questions_data (Any): The json data that comes from the update request
        new_survey (Any): The updated form data, which was added and deleted, along with the question

    Raises:
        TypeError: If `existing_texts` is not an instance of a supported class.
    
    """

    if not isinstance(existing_texts, (Text)):
        raise TypeError("new_text_for_update only works with Scale instances")

    for existing_text in existing_texts:
        new_text_data = next((s for s in questions_data if s.get('id') == existing_text.id), {})
        
        new_text = Text(
            survey_id=new_survey.id,
            order=new_text_data.get('order', existing_text.order),
            type=new_text_data.get('type', existing_text.type),
            input_type=new_text_data.get('input_type', existing_text.input_type),
            text=new_text_data.get('text', existing_text.text),
            
        )
        session.add(new_text)

    for text in existing_texts:
        await session.delete(text)


async def new_email_for_update(session, existing_emails, questions_data, new_survey) -> None:
    """
    Add a new record with the updated data, and delete the previous record specifically for the Email question type
    
    Args:
        session (sqlalchemy.ext.asyncio.AsyncSession): The SQLAlchemy session object.
        existing_emails (Any): The model class representing the question Email
        questions_data (Any): The json data that comes from the update request
        new_survey (Any): The updated form data, which was added and deleted, along with the question

    Raises:
        TypeError: If `existing_emails` is not an instance of a supported class.
    
    """

    for existing_email in existing_emails:
        new_email_data = next((s for s in questions_data if s.get('id') == existing_email.id), {})
        
        new_email = Email(
            survey_id=new_survey.id,
            order=new_email_data.get('order', existing_email.order),
            type=new_email_data.get('type', existing_email.type),
            input_type=new_email_data.get('input_type', existing_email.input_type),
            text=new_email_data.get('text', existing_email.text),
            
        )
        session.add(new_email)

    for email in existing_emails:
        await session.delete(email)


async def new_document_for_update(session, existing_documents, questions_data, new_survey) -> None:
    """
    Add a new record with the updated data, and delete the previous record specifically for the Document question type
    
    Args:
        session (sqlalchemy.ext.asyncio.AsyncSession): The SQLAlchemy session object.
        existing_documents (Any): The model class representing the question Document
        questions_data (Any): The json data that comes from the update request
        new_survey (Any): The updated form data, which was added and deleted, along with the question

    Raises:
        TypeError: If `existing_documents` is not an instance of a supported class.
    
    """

    for existing_document in existing_documents:
        new_document_data = next((s for s in questions_data if s.get('id') == existing_document.id), {})
        
        new_document = Document(
            survey_id=new_survey.id,
            order=new_document_data.get('order', existing_document.order),
            type=new_document_data.get('type', existing_document.type),
            input_type=new_document_data.get('input_type', existing_document.input_type),
            text=new_document_data.get('text', existing_document.text),
            
        )
        session.add(new_document)

    for document in existing_documents:
        await session.delete(document)


async def new_multiple_choice_for_update(session, existing_multiple_choices, questions_data, new_survey) -> None:
    """
    Add a new record with the updated data, and delete the previous record specifically for the Multiple Choice question type
    
    Args:
        session (sqlalchemy.ext.asyncio.AsyncSession): The SQLAlchemy session object.
        existing_multiple_choices (Any): The model class representing the question Multiple Choice
        questions_data (Any): The json data that comes from the update request
        new_survey (Any): The updated form data, which was added and deleted, along with the question

    Raises:
        TypeError: If `existing_multiple_choices` is not an instance of a supported class.
    
    """

    for existing_multiple_choice in existing_multiple_choices:
        new_multiple_choice_data = next((s for s in questions_data if s.get('id') == existing_multiple_choice.id), {})
        
        new_multiple_choice = MultipleChoice(
            survey_id=new_survey.id,
            order=new_multiple_choice_data.get('order', existing_multiple_choice.order),
            type=new_multiple_choice_data.get('type', existing_multiple_choice.type),
            input_type=new_multiple_choice_data.get('input_type', existing_multiple_choice.input_type),
            text=new_multiple_choice_data.get('text', existing_multiple_choice.text),
            
        )
        session.add(new_multiple_choice)

    for multiple_choice in existing_multiple_choices:
        await session.delete(multiple_choice)


async def new_single_choice_for_update(session, existing_single_choices, questions_data, new_survey) -> None:
    """"
    Add a new record with the updated data, and delete the previous record specifically for the Single Choice question type
    
    Args:
        session (sqlalchemy.ext.asyncio.AsyncSession): The SQLAlchemy session object.
        existing_single_choices (Any): The model class representing the question Single Choice
        questions_data (Any): The json data that comes from the update request
        new_survey (Any): The updated form data, which was added and deleted, along with the question

    Raises:
        TypeError: If `existing_single_choices` is not an instance of a supported class.
    
    """

    for existing_single_choice in existing_single_choices:
        new_single_choice_data = next((s for s in questions_data if s.get('id') == existing_single_choice.id), {})
        
        new_single_choice = SingleChoice(
            survey_id=new_survey.id,
            order=new_single_choice_data.get('order', existing_single_choice.order),
            type=new_single_choice_data.get('type', existing_single_choice.type),
            input_type=new_single_choice_data.get('input_type', existing_single_choice.input_type),
            text=new_single_choice_data.get('text', existing_single_choice.text),
            
        )
        session.add(new_single_choice)

    for single_choice in existing_single_choices:
        await session.delete(single_choice)