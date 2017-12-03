import transform

class TestScraper(object):

    def test_should_transform_row_to_dict(self):
        content = "<tr><td>1</td><td>UP 5</td><td>6</td><td>10</td><td>Big Shaq</td><td>Man's Not Hot</td></tr>"

        assert transform.to_entries(content)[0] == {
            "position": 1,
            "movement": 5,
            "previous_position": 6,
            "weeks": 10,
            "artist": "Big Shaq",
            "title": "Man's Not Hot"
        }

    def test_should_transform_row_to_dict_with_negative_movement(self):
        content = "<tr><td>6</td><td>DOWN 5</td><td>1</td><td>10</td><td>marshmello</td><td>Silence (feat. Khalid)</td></tr>"

        assert transform.to_entries(content)[0] == {
            "position": 6,
            "movement": -5,
            "previous_position": 1,
            "weeks": 10,
            "artist": "marshmello",
            "title": "Silence (feat. Khalid)"
        }

    def test_should_transform_row_to_dict_with_no_movement(self):
        content = "<tr><td>1</td><td>NON MOVER</td><td>1</td><td>10</td><td>Big Shaq</td><td>Man's Not Hot</td></tr>"

        assert transform.to_entries(content)[0] == {
            "position": 1,
            "movement": 0,
            "previous_position": 1,
            "weeks": 10,
            "artist": "Big Shaq",
            "title": "Man's Not Hot"
        }

    def test_should_transform_row_with_missing_previous_position_if_new(self):
        content = "<tr><td>1</td><td>NEW</td><td></td><td>1</td><td>Big Shaq</td><td>Man's Not Hot</td></tr>"

        assert transform.to_entries(content)[0] == {
            "position": 1,
            "movement": 0,
            "previous_position": 0,
            "weeks": 1,
            "artist": "Big Shaq",
            "title": "Man's Not Hot"
        }

    def test_should_ignore_header_row(self):
        content = "<tr><td>Position</td><td>Status</td><td>Previous</td><td>Weeks</td><td>Artist</td><td>Title</td></tr>"

        assert not transform.to_entries(content)