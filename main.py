# Utilizando a petstore.swagger.io, faça os testes de
# POST, GET, UPDATE e DELETE desta vez com a entidade Pet

import pytest
import requests

url = 'https://petstore.swagger.io/v2/pet'

def test_post_pet():
    #Configura
    status_code_expected = 200
    category_id_expected = 0
    category_name_expected = 'Dog'
    name_expected = 'Spike'
    photoUrls_expected = ['None']
    tags_expected = [{'id': 0, 'name': 'Dog_Spike'}]
    status_expected = 'available'

    headers = {'Content-Type': 'application/json'}

    # Executa
    response = requests.post(url,
                             data=open('pet1.json', 'rb'),
                             headers=headers)
    response_body = response.json()
    print(response.status_code)
    print(response_body)

    # Valida
    assert response.status_code == status_code_expected
    assert response_body['category']['id'] == category_id_expected
    assert response_body['category']['name'] == category_name_expected
    assert response_body['name'] == name_expected
    assert response_body['photoUrls'] == photoUrls_expected
    assert response_body['tags'] == tags_expected
    assert response_body['status'] == status_expected

    pet_id = response_body['id']
    print(f'pet_id: {pet_id}')
    return pet_id

def test_get_pet():
    # Configura
    pet_id = test_post_pet()
    status_code_expected = 200
    id_expected = pet_id
    category_id_expected = 0
    category_name_expected = 'Dog'
    name_expected = 'Spike'
    photo_urls_expected = ['None']
    tags_expected = [{'id': 0, 'name': 'Dog_Spike'}]
    status_expected = 'available'

    headers = {'Content-Type': 'application/json'}

    # Executa
    response = requests.get(f'{url}/{pet_id}', headers=headers)
    response_body = response.json()
    print(response.status_code)
    print(response_body)

    # Valida
    assert response.status_code == status_code_expected
    assert response_body['id'] == id_expected
    assert response_body['category']['id'] == category_id_expected
    assert response_body['category']['name'] == category_name_expected
    assert response_body['name'] == name_expected
    assert response_body['photoUrls'] == photo_urls_expected
    assert response_body['tags'] == tags_expected
    assert response_body['status'] == status_expected

def test_put_pet():
    pet_id = test_post_pet()
    status_code_expected = 200
    id_expected = pet_id
    category_id_expected = 0
    category_name_expected = 'Dog'
    name_expected = 'Pluto'
    photo_urls_expected = ['None']
    tags_expected = [{'id': 0, 'name': 'Dog_Pluto'}]
    status_expected = 'available'

    headers = {'Content-Type': 'application/json'}

    # Executa
    response = requests.put(url,
                             data=open('pet2.json', 'rb'),
                             headers=headers)
    response_body = response.json()
    print(response.status_code)
    print(response_body)

    # Valida
    assert response.status_code == status_code_expected
    assert response_body['id'] == id_expected
    assert response_body['category']['id'] == category_id_expected
    assert response_body['category']['name'] == category_name_expected
    assert response_body['name'] == name_expected
    assert response_body['photoUrls'] == photo_urls_expected
    assert response_body['tags'] == tags_expected
    assert response_body['status'] == status_expected

def test_delete_pet():
    # Configura
    pet_id = test_post_pet()
    status_code_expected = 200
    type_expected = 'unknown'
    message_expected = str(pet_id)

    headers = {'Content-Type': 'application/json'}

    #Executa
    response = requests.delete(f'{url}/{pet_id}', headers=headers)
    response_body = response.json()
    print(response.status_code)
    print(response_body)

    # Valida
    assert response.status_code == status_code_expected
    assert response_body['code'] == status_code_expected
    assert response_body['type'] == type_expected
    assert response_body['message'] == message_expected