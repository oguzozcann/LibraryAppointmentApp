create table OGRENCI(
	ono numeric(6) not null unique primary key,
	isim text not null,
	soyisim text not null,
	telefon numeric(10) not null unique,
	e_posta text not null unique,
	sifre varchar(20) not null
);

create table SANDALYE(
	sandalye_id char(5) not null unique primary key,
	durum varchar(15) not null check(durum in('dolu','boş','başıboş','terkedilmiş','çevrenin_eşyası'))
	basibos_saati time 
);

create table RANDEVU(
	ono numeric(6) not null references OGRENCI(ono),
	sandalye_id char(5) not null references SANDALYE(sandalye_id),
	tarih date not null,
	baslangic time not null,
	bitis time not null check(bitis>baslangic),
	unique(sandalye_id,tarih,baslangic,bitis),
	primary key(ono,sandalye_id,tarih,baslangic,bitis)
);