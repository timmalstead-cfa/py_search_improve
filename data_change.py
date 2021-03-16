from typing import List
from csv import reader

eng_tags_data: str = ''
span_tags_data: str = ''


def strip_data(data: str) -> str:
    return data.replace("\"", "").replace("'", "").replace('[', '').replace(']', '') + "\n"


try:
    with open("./organization.csv") as csv_data:
        csv_file: List = list(reader(csv_data, delimiter=","))

        for page in csv_file:
            eng_cat, span_cat, eng_tags, span_tags = page[9].split(
                ','), page[10].split(','), page[11].split(','), page[12].split(',')
            new_eng_tags, new_span_tags = [], []
            if('food' in eng_cat):
                eng_food_tags = ['meals', 'nutrition', 'eat',
                                 'hungry', 'hunger', 'snack', 'snacks']
                span_food_tags = ['comidas', 'nutrición', 'comer',
                                  'hambre', 'hambre', 'bocadillo', 'bocadillos']
                new_eng_tags = eng_tags + new_eng_tags + eng_food_tags
                new_span_tags = span_tags + new_span_tags + span_food_tags
            if('substance use' in eng_cat):
                eng_substance_tags = [
                    'drugs', 'alcohol', 'recovery', 'addiction', ]
                span_substance_tags = [
                    'drogas', 'alcohol', 'recuperación', 'adiccion']
                new_eng_tags = eng_tags + new_eng_tags + eng_substance_tags
                new_span_tags = span_tags + new_span_tags + span_substance_tags
            if('medical support' in eng_cat):
                eng_med_tags = ['medical', 'support',
                                'patient', 'patients', 'care', 'illness']
                span_med_tags = ['médico', 'apoyo',
                                 'paciente', 'pacientes', 'cuidado', 'enfermedad']
                new_eng_tags = eng_tags + new_eng_tags + eng_med_tags
                new_span_tags = span_tags + new_span_tags + span_med_tags
            if('transportation' in eng_cat):
                eng_trans_tags = ['transit', 'transport']
                span_trans_tags = ['tránsito', 'transporte']
                new_eng_tags = eng_tags + new_eng_tags + eng_trans_tags
                new_span_tags = span_tags + new_span_tags + span_trans_tags
            if('mental health' in eng_cat):
                eng_mental_health_tags = [
                    'mental', 'health', 'support', 'illness']
                span_mental_health_tags = [
                    'mental', 'salud', 'apoyo', 'enfermedad']
                new_eng_tags = eng_tags + new_eng_tags + eng_mental_health_tags
                new_span_tags = span_tags + new_span_tags + span_mental_health_tags
            if('social services' in eng_cat):
                eng_social_tags = ['social', 'service',
                                   'services', 'community', 'relief']
                span_social_tags = ['social', 'servicio',
                                    'servicios', 'comunidad', 'socorro']
                new_eng_tags = eng_tags + new_eng_tags + eng_social_tags
                new_span_tags = span_tags + new_span_tags + span_social_tags
            if('clothing' in eng_cat):
                eng_clothing_tags = ['clothing',
                                     'clothes', 'shirts', 'pants', 'shoes']
                span_clothing_tags = [
                    'ropa', 'camisas', 'pantalones', 'zapatos']
                new_eng_tags = eng_tags + new_eng_tags + eng_clothing_tags
                new_span_tags = span_tags + new_span_tags + span_clothing_tags
            if('resource directory' in eng_cat):
                eng_resource_tags = ['resource',
                                     'directory', 'resources', 'catalog', 'list']
                span_resource_tags = ['recurso',
                                      'directorio', 'recursos', 'catálogo', 'lista']
                new_eng_tags = eng_tags + new_eng_tags + eng_resource_tags
                new_span_tags = span_tags + new_span_tags + span_resource_tags
            if('legal services' in eng_cat):
                eng_legal_tags = ['legal', 'services',
                                  'advice', 'justice', 'court']
                span_legal_tags = ['legal',
                                   'servicios',
                                   'consejo', 'justicia', 'corte']
                new_eng_tags = eng_tags + new_eng_tags + eng_legal_tags
                new_span_tags = span_tags + new_span_tags + span_legal_tags
            if('community support' in eng_cat):
                eng_community_tags = ['community',
                                      'support', 'neigborhood', 'people']
                span_community_tags = ['comunidad',
                                       'apoyo', 'vecindario', 'gente']
                new_eng_tags = eng_tags + new_eng_tags + eng_community_tags
                new_span_tags = span_tags + new_span_tags + span_community_tags
            if('employment' in eng_cat):
                eng_community_tags = ['employment', 'job', 'jobs', 'trade',
                                      'business', 'hire', 'hiring', 'gig', 'temp', 'full', 'time']
                span_community_tags = [
                    'empleo', 'trabajo', 'trabajos', 'comercio',
                    'negocio', 'contratación', 'contratación', 'concierto', 'temporal', 'completo', 'tiempo']
                new_eng_tags = eng_tags + new_eng_tags + eng_community_tags
                new_span_tags = span_tags + new_span_tags + span_community_tags
            if('housing' in eng_cat):
                eng_housing_tags = ['housing', 'homes',
                                    'apartments', 'rent', 'shelter']
                span_housing_tags = ['vivienda', 'casas',
                                     'apartamentos', 'alquiler', 'refugio']
                new_eng_tags = eng_tags + new_eng_tags + eng_housing_tags
                new_span_tags = span_tags + new_span_tags + span_housing_tags
            if('technology' in eng_cat):
                eng_tech_tags = []
                span_tech_tags = []
                new_eng_tags = eng_tags + new_eng_tags + eng_tech_tags
                new_span_tags = span_tags + new_span_tags + span_tech_tags
            else:
                new_eng_tags = eng_tags + new_eng_tags
                new_span_tags = span_tags + new_span_tags
            new_eng_tags = list(set(new_eng_tags))
            new_span_tags = list(set(new_span_tags))
            eng_tags_data += strip_data(str(new_eng_tags))
            span_tags_data += strip_data(str(new_span_tags))
        with open('eng_tags.csv', 'w') as csv_to_save:
            csv_to_save.write(eng_tags_data)
        with open('span_tags.csv', 'w') as csv_to_save:
            csv_to_save.write(span_tags_data)
except Exception as error:
    print(f"#{error.__class__} occured when trying to parse the csv.")
