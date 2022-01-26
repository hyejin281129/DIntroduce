from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

# 내용등록폼
class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목을 입력해주세요')])
    content = TextAreaField('내용', validators=[DataRequired('내용을 입력해주세요')])

# 답변등록폼
class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용을 입력해주세요')])

# 회원가입 폼
class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired('사용자의 이름을 입력해주세요'), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired('비밀번호를 입력해주세요'), EqualTo('password2', '비밀번호가 일치하지 않습니다')
    ])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired('비밀번호 확인을 입력해주세요')])
    email = EmailField('이메일', validators=[DataRequired('이메일을 입력해주세요'), Email()])

# 로그인 폼
class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired('사용자의 이름을 입력해주세요'), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired('비밀번호를 입력해주세요')])

# 댓글 폼
class CommentForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('댓글을 입력해주세요')])