from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class QuestionForm(FlaskForm):
    # 글자수 제한이 있는 경우 StringField, 없는 경우 Textareafield
    subject = StringField('Subject', validators=[DataRequired("제목은 필수입력 항목입니다.")])
    content = TextAreaField('Content', validators=[DataRequired("내용은 필수입력 항목입니다.")])


class AnswerForm(FlaskForm):
    content = TextAreaField('Content', validators=[DataRequired('내용은 필수입력 항목입니다.')])



class UserCreateForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired("사용자명은 필수입력 항목입니다."), Length(min=3, max=25)])
    password1 = PasswordField('Password', validators=[DataRequired("비밀번호는 필수입력 항목입니다."), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('Password Confirm', validators=[DataRequired("비밀번호 확인은 필수입력 항목입니다.")])
    email = EmailField('이메일', validators=[DataRequired("이메일은 필수입력 항목입니다.")])
    

class UserLoginForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired("사용자명은 필수입력 항목입니다."), Length(min=3, max=25)])
    password = PasswordField('Password', validators=[DataRequired("비밀번호는 필수입력 항목입니다.")])
    