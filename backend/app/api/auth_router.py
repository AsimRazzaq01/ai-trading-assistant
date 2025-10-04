from fastapi import APIRouter, Depends, HTTPException, status, Response, Request


access = create_access_token({"sub": str(user.id)})
resp = RedirectResponse(url="http://localhost:3000/(protected)/dashboard")
set_auth_cookie(resp, access)
return resp
finally:
db.close()


@router.get("/github/login")
async def github_login(request: Request):
    if "github" not in oauth:
    raise HTTPException(400, detail="GitHub OAuth not configured")
redirect_uri = settings.GITHUB_REDIRECT_URI
return await oauth.github.authorize_redirect(request, redirect_uri)


@router.get("/github/callback")
async def github_callback(request: Request):
    if "github" not in oauth:
    raise HTTPException(400, detail="GitHub OAuth not configured")
token = await oauth.github.authorize_access_token(request)
resp = await oauth.github.get("user", token=token)
profile = resp.json()


gh_id = str(profile.get("id"))
name = profile.get("name") or profile.get("login")


email = None
# Try primary email if scope allowed
emails_resp = await oauth.github.get("user/emails", token=token)
for item in emails_resp.json():
    if item.get("primary"):
    email = item.get("email")
break


from app.db.database import SessionLocal
db = SessionLocal()
try:
    user = db.query(User).filter((User.provider == "github") & (User.provider_id == gh_id)).first()
if not user and email:
    user = db.query(User).filter(User.email == email).first()
if not user:
    user = User(name=name, email=email, provider="github", provider_id=gh_id)
db.add(user)
db.commit()
db.refresh(user)
elif not user.provider:
user.provider = "github"
user.provider_id = gh_id
db.commit()


access = create_access_token({"sub": str(user.id)})
resp = RedirectResponse(url="http://localhost:3000/(protected)/dashboard")
set_auth_cookie(resp, access)
return resp
finally:
db.close()