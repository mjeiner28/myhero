from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from sim.models import Tmahasiswa
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed


class mahasiswa_F(FlaskForm):
    npm= StringField('NPM', validators=[DataRequired(),Length(min=10, max=15)])
    nama= StringField('Nama', validators=[DataRequired()])
    email= StringField('Email', validators=[DataRequired(), Email()])
    kelas= StringField('Kelas', validators=[DataRequired()])
    password= PasswordField('Password', validators=[DataRequired(),Length(min=6, max=20)])
    konf_pass= PasswordField('Konfirmasi Password', validators=[DataRequired(), EqualTo('password')])
    alamat= TextAreaField('Alamat')
    submit=SubmitField('Tambah')

    #cek npm
    def validate_npm(self, npm):
        ceknpm=Tmahasiswa.query.filter_by(npm=npm.data).first()
        if ceknpm:
            raise ValidationError('NPM Sudah Terdaftar, Gunakan NPM Yang Lain')

        #cek npm
    def validate_email(self, email):
        cekemail=Tmahasiswa.query.filter_by(email=email.data).first()
        if cekemail:
            raise ValidationError('Email Sudah Terdaftar, Gunakan Email Yang Lain')

class loginmahasiswa_F(FlaskForm):
    npm= StringField('NPM', validators=[DataRequired()])
    password= PasswordField('Password', validators=[DataRequired()])
    submit=SubmitField('Login')

class editmahasiswa_F(FlaskForm):
    npm= StringField('NPM', validators=[DataRequired(),Length(min=10, max=15)])
    nama= StringField('Nama', validators=[DataRequired()])
    email= StringField('Email', validators=[DataRequired(), Email()])
    kelas= StringField('Kelas', validators=[DataRequired()])
    alamat= TextAreaField('Alamat')
    password= PasswordField('Password', validators=[DataRequired(),Length(min=6, max=20)])
    konf_pass= PasswordField('Konfirmasi Password', validators=[DataRequired(), EqualTo('password')])
    foto= FileField('Ubah Foto Profil', validators=[FileAllowed(['jpg', 'png'])])
    submit=SubmitField('Ubah Data')

    #cek npm
    def validate_npm(self, npm):
        if npm.data != current_user.npm:
            ceknpm=Tmahasiswa.query.filter_by(npm=npm.data).first()
            if ceknpm:
                raise ValidationError('NPM Sudah Terdaftar, Gunakan NPM Yang Lain')

    #cek email
    def validate_email(self, email):
        if email.data != current_user.email:
            cekemail=Tmahasiswa.query.filter_by(email=email.data).first()
            if cekemail:
                raise ValidationError('Email Sudah Terdaftar, Gunakan Email Yang Lain')

class pengaduan_F(FlaskForm):
    subjek= StringField('subjek', validators=[DataRequired()])
    kategori= SelectField(u'Kategori Pengaduan', choices=[('administrasi', 'Pelayanan Administrasi'), ('fasilistas', 'Fasilitas'), ('dosen', 'Dosen')], validators=[DataRequired()])
    detail_pengaduan= TextAreaField('pengaduan', validators=[DataRequired()])
    submit=SubmitField('kirim')

class editpengaduan_F(FlaskForm):
    subjek= StringField('subjek', validators=[DataRequired()])
    kategori= SelectField(u'Kategori Pengaduan', choices=[('administrasi', 'Pelayanan Administrasi'), ('fasilistas', 'Fasilitas'), ('dosen', 'Dosen')], validators=[DataRequired()])
    detail_pengaduan= TextAreaField('pengaduan', validators=[DataRequired()])
    submit=SubmitField('Ubah')