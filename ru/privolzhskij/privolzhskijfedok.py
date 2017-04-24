# -*- coding: utf-8 -*-
from tatarstan import tatarstan
from kirovskaja import kirovskaja
from nizhegorodskaja import nizhegorodskaja
from permskij import permskij
from samarskaja import samarskaja
from bashkortostan import bashkortostan
#privolzhskijfedok = {('Privolzhskij fed. ok.', 'Приволжский фед. ок.', 'privolzhskij-fed-ok',): {
privolzhskijfedok = {
    ('Bashkortostan, Resp.', 'Башкортостан, Респ.', 'bashkortostan-resp',): bashkortostan,
    ('CHuvashskaja Resp.', 'Чувашская Респ.', 'chuvashskaja-resp',): {
        ('Alatyr', 'Алатырь', 'alatyr',): {
        },
        ('CHeboksary', 'Чебоксары', 'cheboksary',): {
            ('Kalininskij', 'Калининский', 'kalininskij',): {
            },
            ('Leninskij', 'Ленинский', 'leninskij',): {
            },
            ('Moskovskij', 'Московский', 'moskovskij',): {
            },
        },
        ('JAdrin', 'Ядрин', 'jadrin',): {
        },
        ('Kanash', 'Канаш', 'kanash',): {
        },
        ('Kozlovka', 'Козловка', 'kozlovka',): {
        },
        ('Mariinskij Posad', 'Мариинский Посад', 'mariinskij-posad',): {
        },
        ('Novocheboksarsk', 'Новочебоксарск', 'novocheboksarsk',): {
        },
        ('SHumerlja', 'Шумерля', 'shumerlja',): {
        },
        ('TSivilsk', 'Цивильск', 'tsivilsk',): {
        },
    },
    ('Kirovskaja obl.', 'Кировская обл.', 'kirovskaja-obl',): kirovskaja,
    ('Marij El, Resp.', 'Марий Эл, Респ.', 'marij-el-resp',): {
        ('Joshkar-Ola', 'Йошкар-Ола', 'joshkar-ola',): {
        },
        ('Kozmodemjansk', 'Козьмодемьянск', 'kozmodemjansk',): {
        },
        ('Volzhsk', 'Волжск', 'volzhsk',): {
        },
        ('Zvenigovo', 'Звенигово', 'zvenigovo',): {
        },
    },
    ('Mordovija, Resp.', 'Мордовия, Респ.', 'mordovija-resp',): {
        ('Ardatov', 'Ардатов', 'ardatov',): {
        },
        ('Insar', 'Инсар', 'insar',): {
        },
        ('Kovylkino', 'Ковылкино', 'kovylkino',): {
        },
        ('Krasnoslobodsk', 'Краснослободск', 'krasnoslobodsk',): {
        },
        ('Ruzaevka', 'Рузаевка', 'ruzaevka',): {
        },
        ('Saransk', 'Саранск', 'saransk',): {
        },
        ('Temnikov', 'Темников', 'temnikov',): {
        },
    },
    ('Nizhegorodskaja obl.', 'Нижегородская обл.', 'nizhegorodskaja-obl',): nizhegorodskaja,
    ('Orenburgskaja obl.', 'Оренбургская обл.', 'orenburgskaja-obl',): {
        ('Abdulino', 'Абдулино', 'abdulino',): {
        },
        ('Buguruslan', 'Бугуруслан', 'buguruslan',): {
        },
        ('Buzuluk', 'Бузулук', 'buzuluk',): {
        },
        ('Gaj', 'Гай', 'gaj',): {
        },
        ('JAsnyj', 'Ясный', 'jasnyj',): {
        },
        ('Kuvandyk', 'Кувандык', 'kuvandyk',): {
        },
        ('Mednogorsk', 'Медногорск', 'mednogorsk',): {
        },
        ('Novotroitsk', 'Новотроицк', 'novotroitsk',): {
        },
        ('Orenburg', 'Оренбург', 'orenburg',): {
            ('JUzhnyj', 'Южный', 'juzhnyj',): {
                ('Leninskij', 'Ленинский', 'leninskij',): {
                },
                ('TSentralnyj', 'Центральный', 'tsentralnyj',): {
                },
            },
            ('Severnyj', 'Северный', 'severnyj',): {
                ('Dzerzhinskij', 'Дзержинский', 'dzerzhinskij',): {
                },
                ('Kargala', 'Каргала', 'kargala',): {
                },
                ('Krasnoholm', 'Краснохолм', 'krasnoholm',): {
                },
                ('Promyshlennyj', 'Промышленный', 'promyshlennyj',): {
                },
                ('Prudy', 'Пруды', 'prudy',): {
                },
                ('Samorodovo', 'Самородово', 'samorodovo',): {
                },
            },
        },
        ('Orsk', 'Орск', 'orsk',): {
        },
        ('Sol-Iletsk', 'Соль-Илецк', 'sol-iletsk',): {
        },
        ('Sorochinsk', 'Сорочинск', 'sorochinsk',): {
        },
    },
    ('Penzenskaja obl.', 'Пензенская обл.', 'penzenskaja-obl',): {
        ('Belinskij', 'Белинский', 'belinskij',): {
        },
        ('Gorodische', 'Городище', 'gorodische',): {
        },
        ('Kamenka', 'Каменка', 'kamenka',): {
        },
        ('Kuznetsk', 'Кузнецк', 'kuznetsk',): {
        },
        ('Nikolsk', 'Никольск', 'nikolsk',): {
        },
        ('Nizhnij Lomov', 'Нижний Ломов', 'nizhnij-lomov',): {
        },
        ('Penza', 'Пенза', 'penza',): {
            ('Leninskij', 'Ленинский', 'leninskij',): {
            },
            ('Oktjabrskij', 'Октябрьский', 'oktjabrskij',): {
            },
            ('Pervomajskij', 'Первомайский', 'pervomajskij',): {
            },
            ('ZHeleznodorozhnyj', 'Железнодорожный', 'zheleznodorozhnyj',): {
            },
        },
        ('Serdobsk', 'Сердобск', 'serdobsk',): {
        },
        ('Spassk', 'Спасск', 'spassk',): {
        },
        ('Sursk', 'Сурск', 'sursk',): {
        },
        ('Zarechnyj', 'Заречный', 'zarechnyj',): {
        },
    },
    ('Permskij kraj', 'Пермский край', 'permskij-kraj',): permskij,
    ('Samarskaja obl.', 'Самарская обл.', 'samarskaja-obl',): samarskaja,
    ('Saratovskaja obl.', 'Саратовская обл.', 'saratovskaja-obl',): {
        ('Arkadak', 'Аркадак', 'arkadak',): {
        },
        ('Atkarsk', 'Аткарск', 'atkarsk',): {
        },
        ('Balakovo', 'Балаково', 'balakovo',): {
        },
        ('Balashov', 'Балашов', 'balashov',): {
        },
        ('Engels', 'Энгельс', 'engels',): {
        },
        ('Ershov', 'Ершов', 'ershov',): {
        },
        ('Hvalynsk', 'Хвалынск', 'hvalynsk',): {
        },
        ('Kalininsk', 'Калининск', 'kalininsk',): {
        },
        ('Krasnoarmejsk', 'Красноармейск', 'krasnoarmejsk',): {
        },
        ('Krasnyj Kut', 'Красный Кут', 'krasnyj-kut',): {
        },
        ('Marks', 'Маркс', 'marks',): {
        },
        ('Novouzensk', 'Новоузенск', 'novouzensk',): {
        },
        ('Petrovsk', 'Петровск', 'petrovsk',): {
        },
        ('Pugachev', 'Пугачёв', 'pugachev',): {
        },
        ('Rtischevo', 'Ртищево', 'rtischevo',): {
        },
        ('SHihany', 'Шиханы', 'shihany',): {
        },
        ('Saratov', 'Саратов', 'saratov',): {
            ('Frunzenskij', 'Фрунзенский', 'frunzenskij',): {
            },
            ('Kirovskij', 'Кировский', 'kirovskij',): {
            },
            ('Leninskij', 'Ленинский', 'leninskij',): {
            },
            ('Oktjabrskij', 'Октябрьский', 'oktjabrskij',): {
            },
            ('Volzhskij', 'Волжский', 'volzhskij',): {
            },
            ('Zavodskoj', 'Заводской', 'zavodskoj',): {
            },
        },
        ('Volsk', 'Вольск', 'volsk',): {
        },
    },
    ('Tatarstan, Resp.', 'Татарстан, Респ.', 'tatarstan-resp',): tatarstan,
    ('Udmurtskaja Resp.', 'Удмуртская Респ.', 'udmurtskaja-resp',): {
        ('Glazov', 'Глазов', 'glazov',): {
        },
        ('Izhevsk', 'Ижевск', 'izhevsk',): {
            ('Industrialnyj', 'Индустриальный', 'industrialnyj',): {
            },
            ('Leninskij', 'Ленинский', 'leninskij',): {
            },
            ('Oktjabrskij', 'Октябрьский', 'oktjabrskij',): {
            },
            ('Pervomajskij', 'Первомайский', 'pervomajskij',): {
            },
            ('Ustinovskij', 'Устиновский', 'ustinovskij',): {
            },
        },
        ('Kambarka', 'Камбарка', 'kambarka',): {
        },
        ('Mozhga', 'Можга', 'mozhga',): {
        },
        ('Sarapul', 'Сарапул', 'sarapul',): {
        },
        ('Votkinsk', 'Воткинск', 'votkinsk',): {
        },
    },
    ('Uljanovskaja obl.', 'Ульяновская обл.', 'uljanovskaja-obl',): {
        ('Barysh', 'Барыш', 'barysh',): {
        },
        ('Dimitrovgrad', 'Димитровград', 'dimitrovgrad',): {
        },
        ('Inza', 'Инза', 'inza',): {
        },
        ('Novouljanovsk', 'Новоульяновск', 'novouljanovsk',): {
        },
        ('Sengilej', 'Сенгилей', 'sengilej',): {
        },
        ('Uljanovsk', 'Ульяновск', 'uljanovsk',): {
            ('Leninskij', 'Ленинский', 'leninskij',): {
            },
            ('ZHeleznodorozhnyj', 'Железнодорожный', 'zheleznodorozhnyj',): {
            },
            ('Zasvijazhskij', 'Засвияжский', 'zasvijazhskij',): {
            },
            ('Zavolzhskij', 'Заволжский', 'zavolzhskij',): {
            },
        },
    },
}
