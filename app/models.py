from app import db
from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint
from datetime import datetime


class BphCoconut(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    nama_lengkap = Column(String(40))
    nra = Column(String(9), unique=True)
    wa = Column(String(20), unique=True)
    jurusan = Column(String(15))
    kampus = Column(String(40))
    profile = Column(String)
    depart = Column(String(22))
    def __repr__(self):
        return f"<BPH {self.nama_lengkap}>"


class User(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    nama_lengkap = Column(String(64))
    email = Column(String(64), unique=True)
    nomor_wa = Column(String(20), unique=True)
    asal_kampus = Column(String(64))
    bukti_tf = Column(String(64), default="tidak_ada.jpg")
    bukti_follow = Column(String(64), default="tidak_ada.jpg")
    status = Column(Integer, default=0)
    timestamp = Column(DateTime, default=datetime.utcnow)
    __table_args__ = (UniqueConstraint('nomor_wa', name='unique_nomor_wa'), UniqueConstraint('email',name='unique_email'))
    def __repr__(self):
        return f"<User {self.nama_lengkap}>"
    

class Certificate(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    kode = Column(String(10), unique=True)
    pemilik = Column(String(50))
    keterangan = Column(String(240))
    timestamp = Column(DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f"<Certificate {self.kode}>"