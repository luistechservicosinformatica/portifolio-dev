from flask import Blueprint, request, render_template, redirect, url_for, jsonify
from .models import Post
from . import db

main = Blueprint("main", __name__)

# ------------------ WEB ------------------

@main.route("/")
def home():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)


@main.route("/post/add", methods=["POST"])
def add_post():
    try:
        data = request.form

        post = Post(
            title=data.get("title"),
            content=data.get("content"),
            author=data.get("author")
        )

        db.session.add(post)
        db.session.commit()

    except Exception as e:
        print("Error:", e)

    return redirect(url_for("main.home"))


@main.route("/post/<int:id>/delete")
def delete_post(id):
    try:
        post = Post.query.get_or_404(id)
        db.session.delete(post)
        db.session.commit()
    except Exception as e:
        print("Error:", e)

    return redirect(url_for("main.home"))


@main.route("/post/<int:id>/edit", methods=["GET", "POST"])
def edit_post(id):
    post = Post.query.get_or_404(id)

    if request.method == "POST":
        try:
            data = request.form

            post.title = data.get("title")
            post.content = data.get("content")
            post.author = data.get("author")

            db.session.commit()

        except Exception as e:
            print("Error:", e)

        return redirect(url_for("main.home"))

    return render_template("edit.html", post=post)


# ------------------ API ------------------

@main.route("/api/posts")
def api_posts():
    try:
        posts = Post.query.all()
        return jsonify([p.to_dict() for p in posts])
    except Exception as e:
        print("Error:", e)
        return jsonify([]), 500


@main.route("/api/post", methods=["POST"])
def api_add_post():
    try:
        data = request.get_json()

        post = Post(
            title=data.get("title"),
            content=data.get("content"),
            author=data.get("author")
        )

        db.session.add(post)
        db.session.commit()

        return jsonify({"success": True})

    except Exception as e:
        print("Error:", e)
        return jsonify({"success": False}), 500


@main.route("/api/post/<int:id>", methods=["DELETE"])
def api_delete_post(id):
    try:
        post = Post.query.get_or_404(id)
        db.session.delete(post)
        db.session.commit()

        return jsonify({"success": True})

    except Exception as e:
        print("Error:", e)
        return jsonify({"success": False}), 500


@main.route("/api/post/<int:id>", methods=["PUT"])
def api_edit_post(id):
    try:
        post = Post.query.get_or_404(id)
        data = request.get_json()

        post.title = data.get("title")
        post.content = data.get("content")
        post.author = data.get("author")

        db.session.commit()

        return jsonify({"success": True})

    except Exception as e:
        print("Error:", e)
        return jsonify({"success": False}), 500