from dataclasses import asdict

from flask import Blueprint, jsonify

from repository.player_repository import get_all_players, create_player, get_players_by_position_and_season

players_blueprint = Blueprint("player", __name__)


@players_blueprint.route("/", methods=['GET'])
def get_all_player():
    users = list(map(asdict, get_all_players()))
    return jsonify(users), 200


@players_blueprint.route("/create", methods=['POST'])
def create(user):
    new_id = asdict(create_player(user))
    return jsonify(new_id), 204



@players_blueprint.route("/?position={position}&season={season}", methods=['GET'])
def get_players_by_position(position, season):
    players = get_players_by_position_and_season(position, season)
    return jsonify(players)

