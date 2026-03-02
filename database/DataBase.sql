
create table login (
id int auto_increment not null primary key,
email varchar(60) not null,
senha varchar(255) not null,
cargo enum('user','admin') default 'user'
);

create table criar_denuncia(
id_denuncia int not null auto_increment primary key,
id_user int not null,
nome varchar (100),
data_denuncia datetime not null,
longitude_x decimal (9,6) not null,
latitude_y decimal (9,6) not null,
titulo varchar(40) not null,
descricao text,
status_denuncia enum('pendente','aceita','negada') default 'pendente',
foto varchar(255),

foreign key (id_user) references login(id)
);

create table mapa(
id_user int not null primary key,
id_denuncia int not null,
data_publicacao datetime,
titulo varchar(40),
longitude_x decimal(9,6),
latitude_y decimal(9,6),
descricao text,
foto varchar(255)
);


create table painel_denuncias (
id_user int not null,
id_denuncia int not null primary key,
data_publicacao datetime,
titulo varchar(40),
longitude_x decimal(9,6),
latitude_y decimal(9,6),
status_denuncia enum('pendente','aceita','negada') default 'pendente',
descricao text,
foto varchar(255)
);


delimiter //
create trigger addto_painel_denuncias
after insert on criar_denuncia
for each row
begin
	insert into painel_denuncias (id_user, id_denuncia, data_publicacao, titulo, longitude_x, latitude_y,descricao,foto)
    values (new.id_user,new.id_denuncia, new.data_denuncia, new.titulo,new.longitude_x,new.latitude_y, new.descricao, new.foto);
end//
delimiter ;


insert into criar_denuncia (id_user, data_denuncia,longitude_x,latitude_y,titulo,foto)
values (
10,
'2026-02-28 00:00:00',
-23.667390,
-45.433725,
'Casa 77',
'google.com'
);

insert into login(id,email,senha)
values(
10,
'gabrielcarmoepe@gmail.com',
'11111111111111111111111111111'
);