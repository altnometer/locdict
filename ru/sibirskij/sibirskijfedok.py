# -*- coding: utf-8 -*-
from altajskij import altajskij
from kemerovskaja import kemerovskaja
from krasnojarskij import krasnojarskij
from tomskaja import tomskaja
from irkutskaja import irkutskaja
#sibirskijfedok = {('Sibirskij fed. ok.', 'Сибирский фед. ок.', 'sibirskij-fed-ok',): {
sibirskijfedok = {
    ('Altaj, Resp.', 'Алтай, Респ.', 'altaj-resp',): {
        ('Gorno-Altajsk', 'Горно-Алтайск', 'gorno-altajsk',): {
        },
    },
    ('Altajskij kraj', 'Алтайский край', 'altajskij-kraj',): altajskij,
    ('Burjatija, Resp.', 'Бурятия, Респ.', 'burjatija-resp',): {
        ('Babushkin', 'Бабушкин', 'babushkin',): {
        },
        ('Gusinoozersk', 'Гусиноозёрск', 'gusinoozersk',): {
        },
        ('Kjahta', 'Кяхта', 'kjahta',): {
        },
        ('Severobajkalsk', 'Северобайкальск', 'severobajkalsk',): {
        },
        ('Ulan-Ude', 'Улан-Удэ', 'ulan-ude',): {
            ('Oktjabrskij', 'Октябрьский', 'oktjabrskij',): {
            },
            ('Sovetskij', 'Советский', 'sovetskij',): {
            },
            ('ZHeleznodorozhnyj', 'Железнодорожный', 'zheleznodorozhnyj',): {
            },
        },
        ('Zakamensk', 'Закаменск', 'zakamensk',): {
        },
    },
    ('Hakasija, Resp.', 'Хакасия, Респ.', 'hakasija-resp',): {
        ('Abakan', 'Абакан', 'abakan',): {
        },
        ('Abaza', 'Абаза', 'abaza',): {
        },
        ('CHernogorsk', 'Черногорск', 'chernogorsk',): {
        },
        ('Sajanogorsk', 'Саяногорск', 'sajanogorsk',): {
        },
        ('Sorsk', 'Сорск', 'sorsk',): {
        },
    },
    ('Irkutskaja obl.', 'Иркутская обл.', 'irkutskaja-obl',): irkutskaja,
    ('Kemerovskaja obl.', 'Кемеровская обл.', 'kemerovskaja-obl',): kemerovskaja,
    ('Krasnojarskij kraj', 'Красноярский край', 'krasnojarskij-kraj',): krasnojarskij,
    ('Novosibirskaja obl.', 'Новосибирская обл.', 'novosibirskaja-obl',): {
        ('Barabinsk', 'Барабинск', 'barabinsk',): {
        },
        ('Berdsk', 'Бердск', 'berdsk',): {
        },
        ('Bolotnoe', 'Болотное', 'bolotnoe',): {
        },
        ('CHerepanovo', 'Черепаново', 'cherepanovo',): {
        },
        ('CHulym', 'Чулым', 'chulym',): {
        },
        ('Iskitim', 'Искитим', 'iskitim',): {
        },
        ('Karasuk', 'Карасук', 'karasuk',): {
        },
        ('Kargat', 'Каргат', 'kargat',): {
        },
        ('Kujbyshev', 'Куйбышев', 'kujbyshev',): {
        },
        ('Kupino', 'Купино', 'kupino',): {
        },
        ('Novosibirsk', 'Новосибирск', 'novosibirsk',): {
            ('Dzerzhinskij', 'Дзержинский', 'dzerzhinskij',): {
            },
            ('Kalininskij', 'Калининский', 'kalininskij',): {
            },
            ('Kirovskij', 'Кировский', 'kirovskij',): {
            },
            ('Leninskij', 'Ленинский', 'leninskij',): {
            },
            ('Oktjabrskij', 'Октябрьский', 'oktjabrskij',): {
            },
            ('Pervomajskij', 'Первомайский', 'pervomajskij',): {
            },
            ('Sovetskij', 'Советский', 'sovetskij',): {
            },
            ('TSentralnyj', 'Центральный', 'tsentralnyj',): {
            },
            ('ZHeleznodorozhnyj', 'Железнодорожный', 'zheleznodorozhnyj',): {
            },
            ('Zaeltsovskij', 'Заельцовский', 'zaeltsovskij',): {
            },
        },
        ('Ob', 'Обь', 'ob',): {
        },
        ('Tatarsk', 'Татарск', 'tatarsk',): {
        },
        ('Toguchin', 'Тогучин', 'toguchin',): {
        },
    },
    ('Omskaja obl.', 'Омская обл.', 'omskaja-obl',): {
        ('Isilkul', 'Исилькуль', 'isilkul',): {
        },
        ('Kalachinsk', 'Калачинск', 'kalachinsk',): {
        },
        ('Nazyvaevsk', 'Называевск', 'nazyvaevsk',): {
        },
        ('Omsk', 'Омск', 'omsk',): {
            ('Kirovskij', 'Кировский', 'kirovskij',): {
            },
            ('Leninskij', 'Ленинский', 'leninskij',): {
            },
            ('Oktjabrskij', 'Октябрьский', 'oktjabrskij',): {
            },
            ('Sovetskij', 'Советский', 'sovetskij',): {
                ('Beregovoj', 'Береговой', 'beregovoj',): {
                },
                ('Bolshie polja', 'Большие поля', 'bolshie-polja',): {
                },
                ('Gorodok Neftjanikov', 'Городок Нефтяников', 'gorodok-neftjanikov',): {
                },
                ('Gorodok Vodnikov', 'Городок Водников', 'gorodok-vodnikov',): {
                },
                ('JUbilejnyj (Lukjanovka)', 'Юбилейный (Лукьяновка)', 'jubilejnyj-lukjanovka',): {
                },
                ('Nikolaevka', 'Николаевка', 'nikolaevka',): {
                },
                ('Novoaleksandrovka', 'Новоалександровка', 'novoaleksandrovka',): {
                },
                ('SibNIISHoz', 'СибНИИСХоз', 'sibniishoz',): {
                },
                ('Zahlamino', 'Захламино', 'zahlamino',): {
                },
                ('Zaozernyj', 'Заозёрный', 'zaozernyj',): {
                },
            },
            ('TSentralnyj', 'Центральный', 'tsentralnyj',): {
            },
        },
        ('Tara', 'Тара', 'tara',): {
        },
        ('Tjukalinsk', 'Тюкалинск', 'tjukalinsk',): {
        },
    },
    ('Tomskaja obl.', 'Томская обл.', 'tomskaja-obl',): tomskaja,
    ('Tyva, Resp.', 'Тыва, Респ.', 'tyva-resp',): {
        ('Ak-Dovurak', 'Ак-Довурак', 'ak-dovurak',): {
        },
        ('CHadan', 'Чадан', 'chadan',): {
        },
        ('Kyzyl', 'Кызыл', 'kyzyl',): {
        },
        ('SHagonar', 'Шагонар', 'shagonar',): {
        },
        ('Turan', 'Туран', 'turan',): {
        },
    },
    ('Zabajkalskij kraj', 'Забайкальский край', 'zabajkalskij-kraj',): {
        ('Balej', 'Балей', 'balej',): {
        },
        ('Borzja', 'Борзя', 'borzja',): {
        },
        ('CHita', 'Чита', 'chita',): {
            ('CHernovskij', 'Черновский', 'chernovskij',): {
            },
            ('Ingodinskij', 'Ингодинский', 'ingodinskij',): {
            },
            ('TSentralnyj', 'Центральный', 'tsentralnyj',): {
            },
            ('ZHeleznodorozhnyj', 'Железнодорожный', 'zheleznodorozhnyj',): {
            },
        },
        ('Hilok', 'Хилок', 'hilok',): {
        },
        ('Krasnokamensk', 'Краснокаменск', 'krasnokamensk',): {
        },
        ('Mogocha', 'Могоча', 'mogocha',): {
        },
        ('Nerchinsk', 'Нерчинск', 'nerchinsk',): {
        },
        ('Petrovsk-Zabajkalskij', 'Петровск-Забайкальский', 'petrovsk-zabajkalskij',): {
        },
        ('SHilka', 'Шилка', 'shilka',): {
        },
        ('Sretensk', 'Сретенск', 'sretensk',): {
        },
    },
}
