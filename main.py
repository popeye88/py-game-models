import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    data = json.load(open("players.json", "r")).items()

    for player_name, player_data in data:
        race_data = player_data["race"]
        guild_data = player_data["guild"]

        race = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"]}
        )[0]

        for skill_data in player_data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={"bonus": skill_data["bonus"]},
                race=race,
            )

        if guild_data:
            guild = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]}
            )[0]
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
