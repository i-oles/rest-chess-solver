import unittest
from unittest import TestCase
from app import app
import json


class AppTest(TestCase):
    def test_get_available_moves(self):
        with app.test_client(self) as client:
            resp = client.get("/api/v1/queen/f8")
            self.assertEqual(resp.status_code, 200)

    def test_get_available_moves_contetnt(self):
        with app.test_client(self) as client:
            resp = client.get("/api/v1/rook/A4")
            self.assertEqual(resp.content_type, "application/json")

    def test_get_available_moves_json_data(self):
        with app.test_client(self) as client:
            resp = client.get("/api/v1/knight/A1")
            expected = {
                "availableMoves": ["B3", "C2"],
                "error": "null",
                "figure": "knight",
                "currentField": "A1",
            }

            self.assertEqual(json.loads(resp.get_data()), expected)

    def test_get_available_moves_json_wrong_input(self):
        with app.test_client(self) as client:
            resp = client.get("/api/v1/bishop/f15")
            expected = {
                "availableMoves": [],
                "error": "Field does not exist.",
                "figure": "bishop",
                "currentField": "F15",
            }

            self.assertEqual(json.loads(resp.get_data()), expected)

    def get_validate_move(self):
        with app.test_client(self) as client:
            resp = client.get("/api/v1/knight/c1/d3")
            self.assertEqual(resp.status_code, 200)

    def test_get_validate_move_contetnt(self):
        with app.test_client(self) as client:
            resp = client.get("/api/v1/pawn/A4")
            self.assertEqual(resp.content_type, "application/json")

    def test_get_validate_move_json_data(self):
        with app.test_client(self) as client:
            resp = client.get("/api/v1/king/a2/a3")
            expected = {
                "move": "valid",
                "figure": "king",
                "error": "null",
                "currentField": "A2",
                "destField": "A3",
            }

            self.assertEqual(json.loads(resp.get_data()), expected)

    def test_get_validate_move_json_data(self):
        with app.test_client(self) as client:
            resp = client.get("/api/v1/knight/C4/V8")

            expected = {
                "move": "invalid",
                "figure": "knight",
                "error": "Current move is not permitted.",
                "currentField": "C4",
                "destField": "V8",
            }

            self.assertEqual(json.loads(resp.get_data()), expected)
