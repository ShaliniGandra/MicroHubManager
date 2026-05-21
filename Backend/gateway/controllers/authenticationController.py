from fastapi import APIRouter, Header
from models.schemas import SigninSchema, SignupSchema
import httpx

router = APIRouter(prefix="/authservice")

SPRING_URL = "http://localhost:8081/"  # Base URL for the Spring backend

@router.post("/signup")
async def signup(U: SignupSchema):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            SPRING_URL + "user/signup",
            json=U.model_dump()   # Send data to Spring
        )
    return response.json() # Returs back the response received from spring


@router.post("/signin")
async def signin(U: SigninSchema):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            SPRING_URL + "user/signin",
            json=U.model_dump()   # Send data to Spring
        )
    return response.json() # Returs back the response received from spring

@router.get("/uinfo")
async def uinfo(Token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            SPRING_URL + "user/uinfo",
          headers={"Token": Token}   # Send token to Spring
        )
    return response.json() # Returs back the response received from spring

@router.get("/profile")
async def profile(Token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            SPRING_URL + "user/profile",
          headers={"Token": Token}   # Send token to Spring
        )
    return response.json() # Returs back the response received from spring

@router.get("/getallusers/{PAGE}/{SIZE}")
async def getallusers(PAGE: int, SIZE: int, Token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{SPRING_URL}user/getallusers/{PAGE}/{SIZE}",
            headers = {"Token": Token}
        )
    return response.json()