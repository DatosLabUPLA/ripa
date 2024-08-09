import json
import csv
import pandas as pd
from google.cloud import bigquery

def get_organizations():
    organizations = []

    # Lee el archivo JSON de la versión 1.48 de ROR de la version 2 del esquema de datos
    with open("./v1.49-2024-07-11-ror-data_schema_v2.json") as f:
        data_json = json.load(f)
        for data in data_json:
            organization = {
                "id_ror": None,
                "website": None,
                "acronym_ror": None,
                "name_es": None,
                "name_en": None,
                "geonames_id": None,
                "country_code": None,
                "country_name": None,
                "lat": None,
                "lng": None,
                "name_location": None,
                "last_modified_ror": None,
            }

            if data["locations"][0]["geonames_details"]["country_code"] == "CL" and "education" in data["types"] and data["status"] == "active":

                organization["id_ror"] = data["id"]
                organization["geonames_id"] = data["locations"][0]["geonames_id"]
                organization["country_code"] = data["locations"][0]["geonames_details"]["country_code"]
                organization["country_name"] = data["locations"][0]["geonames_details"]["country_name"]
                organization["lat"] = data["locations"][0]["geonames_details"]["lat"]
                organization["lng"] = data["locations"][0]["geonames_details"]["lng"]
                organization["name_location"] = data["locations"][0]["geonames_details"]["name"]
                organization["last_modified_ror"] = data["admin"]["last_modified"]["date"]

                for links in data["links"]:
                    if links["type"] == "website":
                        organization["website"] = links["value"]

                for name in data["names"]:
                    if "acronym" in name["types"]:
                        organization["acronym_ror"] = name["value"]

                    if "ror_display" in name["types"] and name["lang"] == "es":
                        organization["name_es"] = name["value"]
                    elif "label" in name["types"] and name["lang"] == "es":
                        organization["name_es"] = name["value"]

                    if "ror_display" in name["types"] and name["lang"] == "en":
                        organization["name_en"] = name["value"]
                    elif "label" in name["types"] and name["lang"] == "en":
                        organization["name_en"] = name["value"]
                
                organizations.append(organization)

    return organizations

def save_organizations(organizations):
    # Escribe el archivo CSV por cada organización dentro de la lista de organizaciones. La cabecera del archivo son las llaves del diccionario de la organización.

    with open("organizations_ror.csv", "w", newline="", encoding="UTF-8") as f:
        writer = csv.DictWriter(f, fieldnames=organizations[0].keys())
        writer.writeheader()
        for organization in organizations:
            writer.writerow(organization)

def mix_organizations():
    # obtiene el csv de las organizaciones de ROR y agrega una columna que sea id_gs y acronym dependiento de un filtro
    organizations = pd.read_csv("organizations_ror.csv")
    organizations_gs = pd.read_csv("organizaciones_manual.csv")
    organizations = organizations[["id_ror", "website", "acronym_ror", "name_es", "name_en", "geonames_id", "country_code", "country_name", "lat", "lng", "name_location", "last_modified_ror"]]
    organizations["id_gs"] = None
    organizations["acronym_gs"] = None

    for index, row in organizations.iterrows():
        for index_gs, row_gs in organizations_gs.iterrows():
            if row["name_es"] == "Universidad de Santiago de Chile":
                organizations.at[index, "id_gs"] = "605437563739143535"
                organizations.at[index, "acronym_gs"] = "USACH"
            elif row["name_es"] == "Universidad de Valparaíso":
                organizations.at[index, "id_gs"] = "17388732461633852730"
                organizations.at[index, "acronym_gs"] = "UV"
            elif row["name_es"] == "Universidad de Antofagasta":
                organizations.at[index, "id_gs"] = "7010446216104013295"
                organizations.at[index, "acronym_gs"] = "UANTOF"
            elif row["name_es"] == "Universidad de La Serena":
                organizations.at[index, "id_gs"] = "6030355530770144394"
                organizations.at[index, "acronym_gs"] = "USERENA"
            elif row["name_es"] == "Universidad del Bío-Bío":
                organizations.at[index, "id_gs"] = "8365100606562762008"
                organizations.at[index, "acronym_gs"] = "UBIOBIO"
            elif row["name_es"] == "Universidad de La Frontera":
                organizations.at[index, "id_gs"] = "13908003347799972066"
                organizations.at[index, "acronym_gs"] = "UFRONTERA"
            elif row["name_es"] == "Universidad de Magallanes":
                organizations.at[index, "id_gs"] = "14351944662178497517"
                organizations.at[index, "acronym_gs"] = "UMAG"
            elif row["name_es"] == "Universidad de Talca":
                organizations.at[index, "id_gs"] = "7732664165981901274"
                organizations.at[index, "acronym_gs"] = "UTALCA"
            elif row["name_es"] == "Universidad de Tarapacá":
                organizations.at[index, "id_gs"] = "4727335469935944428"
                organizations.at[index, "acronym_gs"] = "UTA"
            elif row["name_es"] == "Universidad Arturo Prat":
                organizations.at[index, "id_gs"] = "18273373707046377092"
                organizations.at[index, "acronym_gs"] = "UNAP"
            elif row["name_es"] == "Universidad de Playa Ancha de Ciencias de la Educación":
                organizations.at[index, "id_gs"] = "8337597745079551909"
                organizations.at[index, "acronym_gs"] = "UPLA"
            elif row["name_es"] == "Universidad de Los Lagos":
                organizations.at[index, "id_gs"] = "13824009975929506544"
                organizations.at[index, "acronym_gs"] = "ULAGOS"
            elif row["name_es"] == "Pontificia Universidad Católica de Chile":
                organizations.at[index, "id_gs"] = "7459009050823923954"
                organizations.at[index, "acronym_gs"] = "UC"
            elif row["name_es"] == "Universidad de Concepción":
                organizations.at[index, "id_gs"] = "4555896482842878823"
                organizations.at[index, "acronym_gs"] = "UDEC"
            elif row["name_es"] == "Universidad Técnica Federico Santa María":
                organizations.at[index, "id_gs"] = "9225498103198054248"
                organizations.at[index, "acronym_gs"] = "USM"
            elif row["name_es"] == "Pontificia Universidad Católica de Valparaíso":
                organizations.at[index, "id_gs"] = "7698552169257898503"
                organizations.at[index, "acronym_gs"] = "PUCV"
            elif row["name_es"] == "Universidad Austral de Chile":
                organizations.at[index, "id_gs"] = "16206413231987421209"
                organizations.at[index, "acronym_gs"] = "UACH"
            elif row["name_es"] == "Universidad Católica del Norte":
                organizations.at[index, "id_gs"] = "17255630398072300451"
                organizations.at[index, "acronym_gs"] = "UCN"
            elif row["name_es"] == "Universidad Católica del Maule":
                organizations.at[index, "id_gs"] = "12968600147058256171"
                organizations.at[index, "acronym_gs"] = "UCM"
            elif row["name_es"] == "Universidad Católica de la Santísima Concepción":
                organizations.at[index, "id_gs"] = "3702576657308349741"
                organizations.at[index, "acronym_gs"] = "UCSC"
            elif row["name_es"] == "Universidad Católica de Temuco":
                organizations.at[index, "id_gs"] = "12740943834737827853"
                organizations.at[index, "acronym_gs"] = "UCT"
            elif row["name_es"] == "Universidad Santo Tomás":
                organizations.at[index, "id_gs"] = "14018219609791295521"
                organizations.at[index, "acronym_gs"] = "SANTOTOMAS"
            elif row["name_es"] == "Universidad Diego Portales":
                organizations.at[index, "id_gs"] = "12216913016116922734"
                organizations.at[index, "acronym_gs"] = "UDP"
            elif row["name_es"] == "Universidad Andrés Bello":
                organizations.at[index, "id_gs"] = "13542589241086358186"
                organizations.at[index, "acronym_gs"] = "UNAB"
            elif row["name_es"] == "Universidad Autónoma de Chile":
                organizations.at[index, "id_gs"] = "6219877915722792561"
                organizations.at[index, "acronym_gs"] = "UAUTONOMA"
            elif row["name_es"] == "Universidad de Los Andes, Chile":
                organizations.at[index, "id_gs"] = "6615366460316766280"
                organizations.at[index, "acronym_gs"] = "UANDES"
            elif row["name_es"] == "Universidad San Sebastián":
                organizations.at[index, "id_gs"] = "1812728570911196340"
                organizations.at[index, "acronym_gs"] = "USS"
            elif row["name_es"] == "Universidad del Desarrollo":
                organizations.at[index, "id_gs"] = "4794720163447555879"
                organizations.at[index, "acronym_gs"] = "UDD"
            elif row["name_es"] == "Universidad Alberto Hurtado":
                organizations.at[index, "id_gs"] = "15469411678705648791"
                organizations.at[index, "acronym_gs"] = "UAHURTADO"
            elif row["name_es"] == "Universidad Adolfo Ibáñez":
                organizations.at[index, "id_gs"] = "10448777709790852446"
                organizations.at[index, "acronym_gs"] = "UAI"
                

    organizations.to_csv("organizations_mix.csv", index=False)

def upload_bigquery():
    # sube el archivo organizations_mix.csv a bigquery
    organizations = pd.read_csv("organizations_mix.csv")
    organizations.to_gbq("universidades.organizations", project_id="universidades-chile", if_exists="replace", location="US")

def main():
    organizations = get_organizations()
    save_organizations(organizations)
    mix_organizations()

if __name__ == "__main__":
    main()
