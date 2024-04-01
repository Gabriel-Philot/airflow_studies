import pandas as pd
import re


def transform_json_top10(json_result):
    top10_data = []
    for i, item in enumerate(json_result):
        song_name = re.sub(
            r"\b(Remaster(ed)?|\(Remaster(ed)?\)|Deluxe.*|\(Deluxe.*\)|Box Set|\(Box Set\))\b",
            "",
            item["name"],
            flags=re.IGNORECASE,
        )
        album_name = re.sub(
            r"\b(Remaster(ed)?|\(Remaster(ed)?\)|Deluxe.*|\(Deluxe.*\)|Box Set|\(Box Set\))\b",
            "",
            item["album"]["name"],
            flags=re.IGNORECASE,
        )
        release_date = item["album"]["release_date"]
        top10_rank = i + 1  # Assume que a contagem começa do 1
        song_id = item["id"]
        album_id = item["album"]["id"]
        artist_name = item["album"]["artists"][0]["name"]
        artist_id = item["album"]["artists"][0]["id"]

        # Remover parênteses restantes após a substituição
        song_name = (
            song_name.replace("(", "")
            .replace(")", "")
            .replace("'", "")
            .replace("'", "")
        )

        album_name = (
            album_name.replace("(", "")
            .replace(")", "")
            .replace("'", "")
            .replace("'", "")
        )

        song_data = {
            "artist_id": artist_id,
            "name_artist": artist_name,
            "top10_rank": top10_rank,
            "song_name": song_name.strip(),
            "song_id": song_id,
            "album_name": album_name.strip(),
            "album_id": album_id,
            "release_date": release_date,
        }

        top10_data.append(song_data)

    return top10_data


def transform_types(list_of_dicts):

    df = pd.DataFrame(list_of_dicts)

    df["top10_rank"] = df["top10_rank"].astype(int)

    df["release_date"] = pd.to_datetime(df["release_date"]).apply(
        lambda x: x.strftime("%Y-%m-%d")
    )

    df["song_id"] = df["song_id"].astype(str)
    df["album_id"] = df["album_id"].astype(str)

    return df
