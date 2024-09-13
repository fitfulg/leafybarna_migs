// trees_in_parks of Barcelona sample object:
const TIP = {
  "latitud": "41.4372530",
  "nom_cientific": "Populus nigra 'Italica'",
  "codi": "0000024AR",
  "espai_verd": "Central de Nou Barris, Parc",
  "adreca": "Pg Fabra i Puig, 450",
  "catalogacio": "",
  "nom_districte": "NOU BARRIS",
  "tipus_element": "ARBRE PARC",
  "nom_barri": "LA GUINEUETA",
  "geom": "POINT (430266.320389286 4587634.30999226)",
  "longitud": "2.1653025",
  "nom_catala": "Pollancre gavatx",
  "x_etrs89": "430266.320",
  "data_plantacio": null,
  "codi_barri": "48",
  "nom_castella": "Chopo lombardo",
  "codi_districte": "08",
  "tipus_reg": "GOTEIG AVARIAT",
  "categoria_arbrat": "SEGONA",
  "cat_especie_id": 152,
  "tipus_aigua": null,
  "y_etrs89": "4587634.310"
}

// parks_and_gardens of Barcelona sample object:
const PAG = {
  register_id: 99400354567,
  prefix: null,
  suffix: null,
  name: "Jardins de Jaume Vicens Vives",
  created: "2014-10-01T16:24:18+02:00",
  modified: "2022-11-23T12:39:06.437489+01:00",
  status: "published",
  status_name: "Publicat",
  core_type: "place",
  core_type_name: "Equipament",
  body: "<p>Espai obert.Altes accessos: c. Sabino de Arana i Gran Via de Carles III</p>",
  tickets_data: [],
  addresses: [
    {
      place: null,
      district_name: "Les Corts",
      district_id: "04",
      neighborhood_name: "la Maternitat i Sant Ramon",
      neighborhood_id: "20",
      address_name: "Av Diagonal",
      address_id: "144601",
      block_id: null,
      start_street_number: 635,
      end_street_number: null,
      street_number_1: "635",
      street_number_2: null,
      stairs: null,
      level: null,
      door: null,
      zip_code: "08028",
      province: "BARCELONA",
      town: "BARCELONA",
      country: "ESPANYA",
      comments: null,
      position: 0,
      position_relative: "",
      main_address: true,
      road_name: null,
      road_id: null,
      roadtype_name: null,
      roadtype_id: null,
      location: {
        type: "GeometryCollection",
        geometries: [
          {
            type: "Point",
            coordinates: [
              426755.75490054366,
              4582095.394969042
            ]
          }
        ]
      },
      related_entity: null,
      related_entity_data: null,
      hide_address: false,
      transport_data: null
    }
  ],
  entity_types_data: [
    {
      id: 102,
      name: "equipament"
    },
    {
      id: 104,
      name: "parcs"
    },
    {
      id: 100,
      name: "registre"
    }
  ],
  attribute_categories: [
    {
      id: 2,
      name: "Informació d'interès",
      attributes: [
        {
          id: 100003,
          name: "Web",
          description: "Web",
          category: 2,
          type: "url",
          options: [],
          values: [
            {
              id: 95152,
              value: "https://link.bcn.cat/cJdJVV",
              integer_value: null,
              float_value: null,
              char_value: null,
              text_value: null,
              datetime_value: null,
              option_value: null,
              email_value: null,
              phone_value: null,
              url_value: "https://link.bcn.cat/cJdJVV",
              url_visible_value: "https://link.bcn.cat/cJdJVV",
              contact_person_value: null,
              responsible_value: null,
              icon_option_value: null,
              outstanding: true,
              description: "",
              attribute: 100003,
              category_id: 2,
              category_name: "Informació d'interès",
              attribute_name: "Web",
              attribute_type: "url",
              option_value_data: null,
              icon_option_value_data: null,
              responsible_title: null,
              responsible_jobtitle: null
            }
          ]
        },
        {},
        {}
      ]
    }
  ],
  values: [
    {
      id: 95152,
      value: "https://link.bcn.cat/cJdJVV",
      integer_value: null,
      float_value: null,
      char_value: null,
      text_value: null,
      datetime_value: null,
      option_value: null,
      email_value: null,
      phone_value: null,
      url_value: "https://link.bcn.cat/cJdJVV",
      url_visible_value: "https://link.bcn.cat/cJdJVV",
      contact_person_value: null,
      responsible_value: null,
      icon_option_value: null,
      outstanding: true,
      description: "",
      attribute: 100003,
      category_id: 2,
      category_name: "Informació d'interès",
      attribute_name: "Web",
      attribute_type: "url",
      option_value_data: null,
      icon_option_value_data: null,
      responsible_title: null,
      responsible_jobtitle: null
    },
    {},
    {}
  ],
  from_relationships: [
    {
      type_id: 1001,
      name: "És institució de la secció",
      entity_id: 99400355914,
      entity_prefix: null,
      entity_name: "Àrea de Joc Infantil",
      entity_institution: "Jardins de Jaume Vicens Vives",
      entity_suffix: null,
      entity_core_type: "place",
      observation: null,
      start_date: null,
      end_date: null,
      estimated_dates: null,
      addresses: [
        {
          address_name: "Jardins de Jaume Vicens i Vives",
          address_id: "700687",
          street_number: "n 0000",
          district_name: "Les Corts",
          district_id: "04",
          zip_code: "08028",
          town: "Barcelona",
          province: "Barcelona",
          country: "Espanya",
          transport_data: null
        }
      ]
    }
  ],
  to_relationships: [],
  classifications_data: [
    {
      id: 1011006,
      name: "Jardins",
      full_path: "Tipologia EQ >> Ciutat >> Jardins",
      dependency_group: 3033964,
      parent_id: 1011,
      tree_id: 1,
      asia_id: "0000102011006",
      core_type: "place",
      level: 2
    },
    {},
    {},
    {}
  ],
  secondary_filters_data: [
    {
      id: 62080759,
      name: "Parcs i jardins",
      full_path: "Equipaments >> Cultura i lleure >> Parcs i miradors >> Parcs i jardins",
      dependency_group: 3033954,
      parent_id: 29967615,
      tree_id: 401,
      asia_id: "0040103004020002"
    },
    {},
    {},
    {},
    {}
  ],
  timetable: null,
  image_data: null,
  gallery_data: [],
  warnings: [],
  geo_epgs_25831: {
    x: 426755.75490054366,
    y: 4582095.394969042
  },
  geo_epgs_23031: {
    x: 426849.87374333653,
    y: 4582299.714443893
  },
  geo_epgs_4326_latlon: {
    lat: 41.387053996155295,
    lon: 2.123956896300959
  },
  is_section_of_data: null,
  sections_data: [
    {
      id: 99400355914,
      prefix: null,
      suffix: null,
      prefix_ca: null,
      suffix_ca: null,
      name: "Àrea de Joc Infantil",
      status: "published",
      core_type: "place",
      is_section_of_name: "Jardins de Jaume Vicens Vives",
      start_date: "",
      end_date: ""
    }
  ],
  start_date: null,
  end_date: null,
  estimated_dates: null,
  languages_data: null,
  type: null,
  type_name: null,
  period: null,
  period_name: null,
  event_status_name: null,
  event_status: null,
  ical: "BEGIN:VCALENDAR PRODID:ics.py - http://git.io/lLljaA VERSION:2.0 END:VCALENDAR"
}

// local_street_trees of Barcelona sample object (JSON Object):
const ST = {
  "codi": "0000025AR",
  "x_etrs89": 430270.562,
  "y_etrs89": 4587637.9979999997,
  "latitud": 41.4372866,
  "longitud": 2.1653528,
  "tipus_element": "ARBRE VIARI",
  "espai_verd": "Central de Nou Barris, Parc",
  "adreca": "Pg Fabra i Puig, 450",
  "cat_especie_id": 2336,
  "nom_cientific": "Fraxinus angustifolia 'Raywood'",
  "nom_castella": "-",
  "nom_catala": "-",
  "categoria_arbrat": "PRIMERA",
  "data_plantacio": "2022-02-15",
  "tipus_aigua": null,
  "tipus_reg": "GOTEIG AVARIAT",
  "geom": "POINT (430270.561661092 4587637.99844993)",
  "catalogacio": null,
  "codi_barri": 48.0,
  "nom_barri": "LA GUINEUETA",
  "codi_districte": 8.0,
  "nom_districte": "NOU BARRIS"
}

// local_interest_trees of Barcelona sample object:
const LIT = {
  register_id: 99400637926,
  prefix: null,
  suffix: null,
  name: "Araucària de la casa de la Misericòrdia",
  created: "2019-10-01T13:27:28+02:00",
  modified: "2024-02-16T14:43:51.994071+01:00",
  status: "published",
  status_name: "Publicat",
  core_type: "place",
  core_type_name: "Equipament",
  body: "<p>L'araucària de Norfolk és endèmica de la illa australiana de Norfolk. Es caracteritza per la simetria de la seva configuració, amb pisos que es van afegint any rera any, formats per 5 branques que surten del tronc horitzontalment. Aquest exemplar se situa en un jardí privat, a la Casa de la Misericòrdia, en el barri del Raval.</p>",
  tickets_data: [],
  addresses: [
    {
      place: null,
      district_name: "Ciutat Vella",
      district_id: "01",
      neighborhood_name: "el Raval",
      neighborhood_id: "01",
      address_name: "Carrer d'Elisabets",
      address_id: "108506",
      block_id: null,
      start_street_number: 6,
      end_street_number: 6,
      street_number_1: "6",
      street_number_2: null,
      stairs: null,
      level: null,
      door: null,
      zip_code: "08001",
      province: "Barcelona",
      town: "Barcelona",
      country: "Espanya",
      comments: null,
      position: 0,
      position_relative: "",
      main_address: true,
      road_name: null,
      road_id: null,
      roadtype_name: "Carrer",
      roadtype_id: "02",
      location: {
        type: "GeometryCollection",
        geometries: [
          {
            type: "Point",
            coordinates: [
              430499.80738874,
              4581667.660856941
            ]
          }
        ]
      },
      related_entity: null,
      related_entity_data: null,
      hide_address: false,
      transport_data: null
    }
  ],
  entity_types_data: [
    {
      id: 103,
      name: "arbre"
    },
    {},
    {}
  ],
  attribute_categories: [
    {
      id: 5,
      name: "Enriquiment",
      attributes: [
        {
          id: 100040,
          name: "nom-llati",
          description: "nom-llati",
          category: 5,
          type: "char",
          options: [],
          values: [
            {
              id: 432160,
              value: "Araucaria heterophylla",
              integer_value: null,
              float_value: null,
              char_value: "Araucaria heterophylla",
              text_value: null,
              datetime_value: null,
              option_value: null,
              email_value: null,
              phone_value: null,
              url_value: null,
              url_visible_value: null,
              contact_person_value: null,
              responsible_value: null,
              icon_option_value: null,
              outstanding: false,
              description: "",
              attribute: 100040,
              category_id: 5,
              category_name: "Enriquiment",
              attribute_name: "nom-llati",
              attribute_type: "char",
              option_value_data: null,
              icon_option_value_data: null,
              responsible_title: null,
              responsible_jobtitle: null
            }
          ]
        },
        {}
      ]
    },
    {
      id: 2,
      name: "Informació d'interès",
      attributes: [
        {
          id: 100003,
          name: "Web",
          description: "Web",
          category: 2,
          type: "url",
          options: [],
          values: [
            {
              id: 116737,
              value: "http://ajuntament.barcelona.cat/ecologiaurbana",
              integer_value: null,
              float_value: null,
              char_value: null,
              text_value: null,
              datetime_value: null,
              option_value: null,
              email_value: null,
              phone_value: null,
              url_value: "http://ajuntament.barcelona.cat/ecologiaurbana",
              url_visible_value: "ajuntament.barcelona.cat/ecologiaurbana",
              contact_person_value: null,
              responsible_value: null,
              icon_option_value: null,
              outstanding: true,
              description: "",
              attribute: 100003,
              category_id: 2,
              category_name: "Informació d'interès",
              attribute_name: "Web",
              attribute_type: "url",
              option_value_data: null,
              icon_option_value_data: null,
              responsible_title: null,
              responsible_jobtitle: null
            }
          ]
        }
      ]
    },
    {
      id: 1,
      name: "Variables",
      attributes: [
        {
          id: 15,
          name: "Unitats (nombre)",
          description: "Unitats (nombre)",
          category: 1,
          type: "integer",
          options: [],
          values: [
            {
              id: 585559,
              value: 1,
              integer_value: 1,
              float_value: null,
              char_value: null,
              text_value: null,
              datetime_value: null,
              option_value: null,
              email_value: null,
              phone_value: null,
              url_value: null,
              url_visible_value: null,
              contact_person_value: null,
              responsible_value: null,
              icon_option_value: null,
              outstanding: false,
              description: "",
              attribute: 15,
              category_id: 1,
              category_name: "Variables",
              attribute_name: "Unitats (nombre)",
              attribute_type: "integer",
              option_value_data: null,
              icon_option_value_data: null,
              responsible_title: null,
              responsible_jobtitle: null
            }
          ]
        },
        {},
        {},
        {},
        {},
        {}
      ]
    }
  ],
  values: [
    {
      id: 432160,
      value: "Araucaria heterophylla",
      integer_value: null,
      float_value: null,
      char_value: "Araucaria heterophylla",
      text_value: null,
      datetime_value: null,
      option_value: null,
      email_value: null,
      phone_value: null,
      url_value: null,
      url_visible_value: null,
      contact_person_value: null,
      responsible_value: null,
      icon_option_value: null,
      outstanding: false,
      description: "",
      attribute: 100040,
      category_id: 5,
      category_name: "Enriquiment",
      attribute_name: "nom-llati",
      attribute_type: "char",
      option_value_data: null,
      icon_option_value_data: null,
      responsible_title: null,
      responsible_jobtitle: null
    },
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {}
  ],
  from_relationships: [],
  to_relationships: [],
  classifications_data: [
    {
      id: 1011063,
      name: "Arbres d'interès local ",
      full_path: "Tipologia EQ >> Ciutat >> Arbres d'interès local ",
      dependency_group: 3033964,
      parent_id: 1011,
      tree_id: 1,
      asia_id: "0000102011063",
      core_type: "place",
      level: 2
    }
  ],
  secondary_filters_data: [
    {
      id: 29972600,
      name: "Arbres d'interès local",
      full_path: "Equipaments >> Animals i plantes >> Arbres d'interès local",
      dependency_group: 3033954,
      parent_id: 401009,
      tree_id: 401,
      asia_id: "0040102009005"
    }
  ],
  timetable: null,
  image_data: null,
  gallery_data: [],
  warnings: [],
  geo_epgs_25831: {
    x: 430499.80738874,
    y: 4581667.660856941
  },
  geo_epgs_23031: {
    x: 430593.92367209465,
    y: 4581872.009403022
  },
  geo_epgs_4326_latlon: {
    lat: 41.383533724779035,
    lon: 2.168782330504542
  },
  is_section_of_data: null,
  sections_data: [],
  start_date: null,
  end_date: null,
  estimated_dates: null,
  languages_data: null,
  type: null,
  type_name: null,
  period: null,
  period_name: null,
  event_status_name: null,
  event_status: null,
  ical: "BEGIN:VCALENDAR PRODID:ics.py - http://git.io/lLljaA VERSION:2.0END:VCALENDAR"
}