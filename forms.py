from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField
from wtforms.validators import DataRequired, AnyOf, URL


class ShowForm(Form):
    venue_id = StringField("venue_id", validators=[DataRequired()])
    venue_name = StringField("venue_name", validators=[DataRequired()])
    artist_id = StringField("artist_id", validators=[DataRequired()])
    artist_name = StringField("artist_name", validators=[DataRequired()])
    artist_image_link = StringField("artist_image_link", validators=[URL()])
    start_time = DateTimeField(
        "start_time", validators=[DataRequired()], default=datetime.today()
    )


class VenueForm(Form):
    name = StringField("name", validators=[DataRequired()])
    genres = SelectMultipleField(
        # TODO implement enum restriction
        "genres",
        validators=[DataRequired()],
        choices=[
            ("Alternative", "Alternative"),
            ("Blues", "Blues"),
            ("Classical", "Classical"),
            ("Country", "Country"),
            ("Electronic", "Electronic"),
            ("Folk", "Folk"),
            ("Funk", "Funk"),
            ("Hip-Hop", "Hip-Hop"),
            ("Heavy Metal", "Heavy Metal"),
            ("Instrumental", "Instrumental"),
            ("Jazz", "Jazz"),
            ("Musical Theatre", "Musical Theatre"),
            ("Pop", "Pop"),
            ("Punk", "Punk"),
            ("R&B", "R&B"),
            ("Reggae", "Reggae"),
            ("Rock n Roll", "Rock n Roll"),
            ("Soul", "Soul"),
            ("Other", "Other"),
        ],
    )
    address = StringField("address", validators=[DataRequired()])
    city = StringField("city", validators=[DataRequired()])
    state = SelectField(
        "state",
        validators=[DataRequired()],
        choices=[
            ("AL", "AL"),
            ("AK", "AK"),
            ("AZ", "AZ"),
            ("AR", "AR"),
            ("CA", "CA"),
            ("CO", "CO"),
            ("CT", "CT"),
            ("DE", "DE"),
            ("DC", "DC"),
            ("FL", "FL"),
            ("GA", "GA"),
            ("HI", "HI"),
            ("ID", "ID"),
            ("IL", "IL"),
            ("IN", "IN"),
            ("IA", "IA"),
            ("KS", "KS"),
            ("KY", "KY"),
            ("LA", "LA"),
            ("ME", "ME"),
            ("MT", "MT"),
            ("NE", "NE"),
            ("NV", "NV"),
            ("NH", "NH"),
            ("NJ", "NJ"),
            ("NM", "NM"),
            ("NY", "NY"),
            ("NC", "NC"),
            ("ND", "ND"),
            ("OH", "OH"),
            ("OK", "OK"),
            ("OR", "OR"),
            ("MD", "MD"),
            ("MA", "MA"),
            ("MI", "MI"),
            ("MN", "MN"),
            ("MS", "MS"),
            ("MO", "MO"),
            ("PA", "PA"),
            ("RI", "RI"),
            ("SC", "SC"),
            ("SD", "SD"),
            ("TN", "TN"),
            ("TX", "TX"),
            ("UT", "UT"),
            ("VT", "VT"),
            ("VA", "VA"),
            ("WA", "WA"),
            ("WV", "WV"),
            ("WI", "WI"),
            ("WY", "WY"),
        ],
    )
    phone = StringField("phone", validators=[DataRequired()])
    website = StringField(
        # TODO implement validation logic for state
        "website",
        validators=[DataRequired()],
    )
    facebook_link = StringField(
        # TODO implement enum restriction
        "facebook_link",
        validators=[URL()],
    )
    seeking_talent = StringField(
        # TODO implement enum restriction
        "seeking_talent",
        validators=[DataRequired()],
    )
    seeking_description = StringField(
        # TODO implement enum restriction
        "seeking_description",
        validators=[DataRequired()],
    )
    image_link = StringField("image_link")


class ArtistForm(Form):
    name = StringField("name", validators=[DataRequired()])
    genres = SelectMultipleField(
        # TODO implement enum restriction
        "genres",
        validators=[DataRequired()],
        choices=[
            ("Alternative", "Alternative"),
            ("Blues", "Blues"),
            ("Classical", "Classical"),
            ("Country", "Country"),
            ("Electronic", "Electronic"),
            ("Folk", "Folk"),
            ("Funk", "Funk"),
            ("Hip-Hop", "Hip-Hop"),
            ("Heavy Metal", "Heavy Metal"),
            ("Instrumental", "Instrumental"),
            ("Jazz", "Jazz"),
            ("Musical Theatre", "Musical Theatre"),
            ("Pop", "Pop"),
            ("Punk", "Punk"),
            ("R&B", "R&B"),
            ("Reggae", "Reggae"),
            ("Rock n Roll", "Rock n Roll"),
            ("Soul", "Soul"),
            ("Other", "Other"),
        ],
    )
    city = StringField("city", validators=[DataRequired()])
    state = SelectField(
        "state",
        validators=[DataRequired()],
        choices=[
            ("AL", "AL"),
            ("AK", "AK"),
            ("AZ", "AZ"),
            ("AR", "AR"),
            ("CA", "CA"),
            ("CO", "CO"),
            ("CT", "CT"),
            ("DE", "DE"),
            ("DC", "DC"),
            ("FL", "FL"),
            ("GA", "GA"),
            ("HI", "HI"),
            ("ID", "ID"),
            ("IL", "IL"),
            ("IN", "IN"),
            ("IA", "IA"),
            ("KS", "KS"),
            ("KY", "KY"),
            ("LA", "LA"),
            ("ME", "ME"),
            ("MT", "MT"),
            ("NE", "NE"),
            ("NV", "NV"),
            ("NH", "NH"),
            ("NJ", "NJ"),
            ("NM", "NM"),
            ("NY", "NY"),
            ("NC", "NC"),
            ("ND", "ND"),
            ("OH", "OH"),
            ("OK", "OK"),
            ("OR", "OR"),
            ("MD", "MD"),
            ("MA", "MA"),
            ("MI", "MI"),
            ("MN", "MN"),
            ("MS", "MS"),
            ("MO", "MO"),
            ("PA", "PA"),
            ("RI", "RI"),
            ("SC", "SC"),
            ("SD", "SD"),
            ("TN", "TN"),
            ("TX", "TX"),
            ("UT", "UT"),
            ("VT", "VT"),
            ("VA", "VA"),
            ("WA", "WA"),
            ("WV", "WV"),
            ("WI", "WI"),
            ("WY", "WY"),
        ],
    )
    phone = StringField(
        # TODO implement validation logic for state
        "phone",
        validators=[DataRequired()],
    )
    website = StringField(
        # TODO implement validation logic for state
        "website",
        validators=[URL()],
    )
    facebook_link = StringField(
        # TODO implement enum restriction
        "facebook_link",
        validators=[URL()],
    )
    seeking_venue = StringField(
        # TODO implement enum restriction
        "seeking_venue",
        validators=[DataRequired()],
    )
    seeking_description = StringField(
        # TODO implement enum restriction
        "seeking_description",
        validators=[DataRequired()],
    )
    image_link = StringField(
        "image_link",
        validators=[URL()],
    )


# TODO IMPLEMENT NEW ARTIST FORM AND NEW SHOW FORM
