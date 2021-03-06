# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#

import json
import dateutil.parser

import babel


from flask import (
    Flask,
    render_template,
    request,
    Response,
    flash,
    redirect,
    url_for,
    jsonify,
    abort,
)
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from forms import *
from flask_migrate import Migrate
import sys
from config import SQLALCHEMY_DATABASE_URI
from models import app, db, Venue, Artist, Show

# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object("config")
db.init_app(app)
# connect to db
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI

# db = SQLAlchemy(app)

# migrate = Migrate(app, db)


# TODO: connect to a local postgresql database

# ----------------------------------------------------------------------------#
# Models.
# ----------------------------------------------------------------------------#


# TODO: implement any missing fields, as a database migration using Flask-Migrate


# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.


# ----------------------------------------------------------------------------#
# Filters.
# ----------------------------------------------------------------------------#


def format_datetime(value, format="medium"):
    date = dateutil.parser.parse(value)
    if format == "full":
        format = "EEEE MMMM, d, y 'at' h:mma"
    elif format == "medium":
        format = "EE MM, dd, y h:mma"
    return babel.dates.format_datetime(date, format)


app.jinja_env.filters["datetime"] = format_datetime

# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#


@app.route("/")
def index():
    return render_template("pages/home.html")


#  Venues
#  ----------------------------------------------------------------


#  Get Venues
#  ----------------------------------------------------------------


@app.route("/venues", methods=["GET"])
def venues():
    # TODO: show list of venues.

    # data = Venue.query.order_by("state").all()
    locals = []
    venues = Venue.query.all()
    for place in Venue.query.distinct(Venue.city, Venue.state).all():
        locals.append(
            {
                "city": place.city,
                "state": place.state,
                "venues": [
                    {
                        "id": venue.id,
                        "name": venue.name,
                    }
                    for venue in venues
                    if venue.city == place.city and venue.state == place.state
                ],
            }
        )
    return render_template("pages/venues.html", areas=locals)


#  Search Venues
#  ----------------------------------------------------------------


@app.route("/venues/search", methods=["POST"])
def search_venues():
    # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
    # seach for Hop should return "The Musical Hop".
    # search for "Music" should return "The Musical Hop" and "Park Square Live Music & Coffee"

    search = request.form.get("search_term", "")
    result = Venue.query.filter(Venue.name.ilike("%" + search + "%")).all()
    response = {"count": len(result), "data": result}
    return render_template(
        "pages/search_venues.html",
        results=response,
        search_term=request.form.get("search_term", ""),
    )


# Get venue page with venue_id
#  ----------------------------------------------------------------


@app.route("/venues/<venue_id>")
def show_venue(venue_id):

    # TODO: replace with real venue data from the venues table, using venue_id

    from datetime import datetime

    past_shows = (
        db.session.query(Artist, Show)
        .join(Show)
        .join(Venue)
        .filter(
            Show.venue_id == venue_id,
            Show.artist_id == Artist.id,
            Show.start_time < datetime.now(),
        )
        .all()
    )

    upcoming_shows = (
        db.session.query(Artist, Show)
        .join(Show)
        .join(Venue)
        .filter(
            Show.venue_id == venue_id,
            Show.artist_id == Artist.id,
            Show.start_time > datetime.now(),
        )
        .all()
    )

    venue = Venue.query.filter_by(id=venue_id).first_or_404()

    data = {
        "id": venue.id,
        "name": venue.name,
        "genres": venue.genres,
        "address": venue.address,
        "city": venue.city,
        "state": venue.state,
        "phone": venue.phone,
        "website": venue.website,
        "facebook_link": venue.facebook_link,
        "seeking_talent": venue.seeking_talent,
        "seeking_description": venue.seeking_description,
        "image_link": venue.image_link,
        "past_shows": [
            {
                "id": artist.id,
                "name": artist.name,
                "image_link": artist.image_link,
                "start_time": show.start_time.strftime("%m/%d/%Y, %H:%M"),
            }
            for artist, show in past_shows
        ],
        "upcoming_shows": [
            {
                "id": artist.id,
                "name": artist.name,
                "image_link": artist.image_link,
                "start_time": show.start_time.strftime("%m/%d/%Y, %H:%M"),
            }
            for artist, show in upcoming_shows
        ],
        "past_shows_count": len(past_shows),
        "upcoming_shows_count": len(upcoming_shows),
    }

    return render_template("pages/show_venue.html", venue=data)


#  Call Venue form
#  ----------------------------------------------------------------


@app.route("/venues/create", methods=["GET"])
def create_venue_form():
    form = VenueForm()
    return render_template("forms/new_venue.html", form=form)


#  Create Venue
#  ----------------------------------------------------------------


@app.route("/venues/create", methods=["POST"])
def create_venue_submission():
    # TODO: insert form data as a new Venue record in the db, instead
    # TODO: modify data to be the data object returned from db insertion

    form = VenueForm(request.form)
    try:
        venue = Venue()
        form.populate_obj(venue)
        db.session.add(venue)
        db.session.commit()
        flash("Venue " + request.form["name"] + " was successfully listed!")
    except ValueError as e:
        print(e)
        flash(
            "An error occurred. Venue " + request.form["name"] + " could not be listed."
        )
        db.session.rollback()
    finally:
        db.session.close()
    return render_template("pages/home.html")


#  Delete Venue with venue id
#  ----------------------------------------------------------------


@app.route("/venues/<venue_id>", methods=["DELETE"])
def delete_venue(venue_id):
    # TODO: Complete this endpoint for taking a venue_id, and using
    # SQLAlchemy ORM to delete a record. Handle cases where the session commit could fail.
    error = False
    try:
        deleteVenueId = Venue.query.get(venue_id)

        db.session.delete(deleteVenueId)

        db.session.commit()
        # return True

    except:
        db.session.rollback()
        error = True
    finally:
        db.session.close()
    if error:
        # flash(
        #     "An error occurred. Venue " + deleteVenueId.name + " could not be deleted."
        # )
        flash("An error occurred. Venue  could not be deleted.")
    else:
        # flash("Venue " + deleteVenueId.name + " was successfully deleted!")
        flash("Venue was successfully deleted!")

    # BONUS CHALLENGE: Implement a button to delete a Venue on a Venue Page, have it so that
    # clicking that button delete it from the db then redirect the user to the homepage
    return redirect(url_for("index"))


#  Artists
#  ----------------------------------------------------------------


#  Call Artist form
#  ----------------------------------------------------------------


@app.route("/artists/create", methods=["GET"])
def create_artist_form():
    form = ArtistForm()
    return render_template("forms/new_artist.html", form=form)


#  Create Artist
#  ----------------------------------------------------------------


@app.route("/artists/create", methods=["POST"])
def create_artist_submission():
    # called upon submitting the new artist listing form
    # TODO: insert form data as a new Venue record in the db, instead
    # TODO: modify data to be the data object returned from db insertion

    form = ArtistForm(request.form)
    try:
        artist = Artist()
        form.populate_obj(artist)
        db.session.add(artist)
        db.session.commit()
        flash("Artist " + request.form["name"] + " was successfully listed!")
    except ValueError as e:
        print(e)
        flash(
            "An error occurred. Artist "
            + request.form["name"]
            + " could not be listed."
        )
        db.session.rollback()
    finally:
        db.session.close()

    return render_template("pages/home.html")


#  Get Artists
#  ----------------------------------------------------------------


@app.route("/artists", methods=["GET"])
def artists():
    # TODO: replace with real data returned from querying the database
    data = Artist.query.order_by("id").all()
    return render_template("pages/artists.html", artists=data)


@app.route("/artists/search", methods=["POST"])
def search_artists():
    # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
    # seach for "A" should return "Guns N Petals", "Matt Quevado", and "The Wild Sax Band".
    # search for "band" should return "The Wild Sax Band".

    search = request.form.get("search_term", "")
    result = Artist.query.filter(Artist.name.ilike("%" + search + "%")).all()
    response = {"count": len(result), "data": result}
    return render_template(
        "pages/search_artists.html",
        results=response,
        search_term=request.form.get("search_term", ""),
    )


@app.route("/artists/<artist_id>")
def show_artist(artist_id):
    # shows the venue page with the given venue_id
    # TODO: replace with real venue data from the venues table, using venue_id
    from datetime import datetime

    past_shows = (
        db.session.query(Artist, Show)
        .join(Show)
        .join(Venue)
        .filter(
            Show.artist_id == artist_id,
            Show.venue_id == Venue.id,
            Show.start_time < datetime.now(),
        )
        .all()
    )

    upcoming_shows = (
        db.session.query(Artist, Show)
        .join(Show)
        .join(Venue)
        .filter(
            Show.artist_id == artist_id,
            Show.venue_id == Venue.id,
            Show.start_time > datetime.now(),
        )
        .all()
    )

    artist = Artist.query.filter_by(id=artist_id).first_or_404()

    data = {
        "id": artist.id,
        "name": artist.name,
        "genres": artist.genres,
        "city": artist.city,
        "state": artist.state,
        "phone": artist.phone,
        "website": artist.website,
        "facebook_link": artist.facebook_link,
        "seeking_venue": artist.seeking_venue,
        "seeking_description": artist.seeking_description,
        "image_link": artist.image_link,
        "past_shows": [
            {
                "id": artist.id,
                "name": artist.name,
                "image_link": artist.image_link,
                "start_time": show.start_time.strftime("%m/%d/%Y, %H:%M"),
            }
            for artist, show in past_shows
        ],
        "upcoming_shows": [
            {
                "id": artist.id,
                "name": artist.name,
                "image_link": artist.image_link,
                "start_time": show.start_time.strftime("%m/%d/%Y, %H:%M"),
            }
            for artist, show in upcoming_shows
        ],
        "past_shows_count": len(past_shows),
        "upcoming_shows_count": len(upcoming_shows),
    }

    return render_template("pages/show_artist.html", artist=data)


#  Load artist form
#  ----------------------------------------------------------------


@app.route("/artists/<artist_id>/edit", methods=["GET"])
def edit_artist(artist_id):
    artist = Artist.query.first_or_404(artist_id)
    form = ArtistForm(obj=artist)

    # TODO: populate form with fields from artist with ID <artist_id>
    return render_template("forms/edit_artist.html", form=form, artist=artist)


#  Update artist with artist_id
#  ----------------------------------------------------------------


@app.route("/artists/<artist_id>/edit", methods=["POST"])
def edit_artist_submission(artist_id):
    # TODO: take values from the form submitted, and update existing
    # artist record with ID <artist_id> using the new attributes
    form = ArtistForm(request.form)

    try:
        artist = Artist.query.first_or_404(artist_id)
        form.populate_obj(artist)
        db.session.commit()
        flash(f"Venue {form.name.data} was successfully edited!")

    except ValueError as e:
        db.session.rollback()
        flash(f"An error occurred in {form.name.data}. Error: {str(e)}")

    finally:
        db.session.close()

    return redirect(url_for("show_artist", artist_id=artist_id))


#  Load venue form
#  ----------------------------------------------------------------


@app.route("/venues/<venue_id>/edit", methods=["GET"])
def edit_venue(venue_id):

    venue = Venue.query.first_or_404(venue_id)
    form = VenueForm(obj=venue)

    # TODO: populate form with values from venue with ID <venue_id>
    return render_template("forms/edit_venue.html", form=form, venue=venue)


#  Update venue with venue_id
#  ----------------------------------------------------------------


@app.route("/venues/<venue_id>/edit", methods=["POST"])
def edit_venue_submission(venue_id):
    # TODO: take values from the form submitted, and update existing
    # venue record with ID <venue_id> using the new attributes

    form = VenueForm(request.form)

    try:
        venue = Venue.query.first_or_404(venue_id)
        form.populate_obj(venue)
        db.session.commit()
        flash(f"Venue {form.name.data} was successfully edited!")

    except ValueError as e:
        db.session.rollback()
        flash(f"An error occurred in {form.name.data}. Error: {str(e)}")

    finally:
        db.session.close()

    return redirect(url_for("show_venue", venue_id=venue_id))


#  Get Shows
#  ----------------------------------------------------------------


@app.route("/shows", methods=["GET"])
def shows():
    # displays list of shows at /shows
    # TODO: replace with real venues data.
    #       num_shows should be aggregated based on number of upcoming shows per venue.

    data = Show.query.order_by("id").all()

    return render_template("pages/shows.html", shows=data)


#  Load Show form
#  ----------------------------------------------------------------


@app.route("/shows/create")
def create_shows():
    # renders form. do not touch.
    form = ShowForm()
    return render_template("forms/new_show.html", form=form)


#  Create Shows
#  ----------------------------------------------------------------


@app.route("/shows/create", methods=["POST"])
def create_show_submission():
    # called to create new shows in the db, upon submitting new show listing form
    # TODO: insert form data as a new Show record in the db, instead
    error = False
    try:
        artist_id = request.form.get("artist_id")
        venue_id = request.form.get("venue_id")
        start_time = request.form.get("start_time")

        newShow = Show(
            artist_id=artist_id,
            venue_id=venue_id,
            start_time=start_time,
        )
        db.session.add(newShow)

        db.session.commit()

    except:
        db.session.rollback()
        error = True
    finally:
        db.session.close()
    if error:
        # TODO: on unsuccessful db insert, flash an error instead.
        flash("An error occurred. Show could not be listed.")
    else:
        # on successful db insert, flash success
        flash("Show was successfully listed!")

    # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
    return render_template("pages/home.html")


@app.errorhandler(404)
def not_found_error(error):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def server_error(error):
    return render_template("errors/500.html"), 500


if not app.debug:
    file_handler = FileHandler("error.log")
    file_handler.setFormatter(
        Formatter("%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]")
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info("errors")

# ----------------------------------------------------------------------------#
# Launch.
# ----------------------------------------------------------------------------#

# Default port:
if __name__ == "__main__":
    app.run()

# Or specify port manually:
"""
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
"""
