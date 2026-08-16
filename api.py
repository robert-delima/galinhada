import sqlite3

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date

app = FastAPI()

conexao = sqlite3.connect(
    "galinhada.db",
    check_same_thread=False
)

cursor = conexao.cursor()

class Producao(BaseModel):
    quantidade_galinhas: int
    quantidade_ovos: int
    racao_kg: float

class AtualizarOvos(BaseModel):
    quantidade_ovos: int

class AtualizarGalinhas(BaseModel):
    quantidade_galinhas: int

class AtualizarRacao(BaseModel):
    racao_kg: float

class AtualizarData(BaseModel):
    data: date

@app.get("/producoes")
def listar_producoes():
    cursor.execute("""
        SELECT *
        FROM producao
    """)

    resultado = cursor.fetchall()

    producoes = []

    for registro in resultado:
        producoes.append({
            "id": registro[0],
            "data": registro[1],
            "quantidade_galinhas": registro[2],
            "quantidade_ovos": registro[3],
            "racao_kg": registro[4]
        })

    return producoes

@app.get("/producoes/{id}")
def buscar_producao(id: int):
    cursor.execute("""
        SELECT *
        FROM producao
        WHERE id = ?
    """,(id,))

    resultado = cursor.fetchone()

    if resultado is None:
        raise HTTPException(
            status_code=404,
            detail="Produção não encontrada"
        )

    return {
        "id": resultado[0],
        "data": resultado[1],
        "quantidade_galinhas": resultado[2],
        "quantidade_ovos": resultado[3],
        "racao_kg": resultado[4]
    }

@app.post("/producoes")
def registrar_producao(producao: Producao):
    data = date.today().isoformat()

    cursor.execute("""
        INSERT INTO producao
            (data, 
             quantidade_galinhas,
             quantidade_ovos,
             racao_kg)
        VALUES (?, ?, ?, ?)
    """,(data,
         producao.quantidade_galinhas,
         producao.quantidade_ovos,
         producao.racao_kg))

    conexao.commit()
    id_criado = cursor.lastrowid

    return {
        "mensagem": "Produção cadastrada com sucesso",
        "id": id_criado
    }

@app.patch("/producoes/{id}/ovos")
def atualizar_ovos(id: int, producao: AtualizarOvos):
    cursor.execute("""
        UPDATE producao
        SET quantidade_ovos = ?
        WHERE id = ?
    """,(producao.quantidade_ovos,
         id))

    if cursor.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail="Produção não encontrada"
        )

    conexao.commit()

    return {
        "mensagem": "Quantidade de ovos atualizada",
        "id": id
    }

@app.patch("/producoes/{id}/racao")
def atualizar_racao(id: int, producao: AtualizarRacao):
    cursor.execute("""
        UPDATE producao
        SET racao_kg = ?
        WHERE id = ?
    """, (producao.racao_kg, id))

    if cursor.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail="Produção não encontrada"
        )

    conexao.commit()

    return {
        "mensagem": "Ração atualizada",
        "id": id
    }

@app.patch("/producoes/{id}/galinhas")
def atualizar_galinhas(id: int, producao: AtualizarGalinhas):
    cursor.execute("""
        UPDATE producao
        SET quantidade_galinhas = ?
        WHERE id = ?
    """, (producao.quantidade_galinhas, id))

    if cursor.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail="Produção não encontrada"
        )

    conexao.commit()

    return {
        "mensagem": "Galinhas atualizada",
        "id": id
    }

@app.patch("/producoes/{id}/data")
def atualizar_data(id: int, producao: AtualizarData):
    cursor.execute("""
        UPDATE producao
        SET data = ?
        WHERE id = ?
    """, (producao.data, id))

    if cursor.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail="Produção não encontrada"
        )

    conexao.commit()

    return {
        "mensagem": "Data atualizada",
        "id": id
    }

@app.delete("/producoes/{id}")
def deletar_producao(id: int):
    cursor.execute("""
        DELETE
        FROM producao
        WHERE id = ?
    """, (id,))

    if cursor.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail="Produção não encontrada"
        )

    conexao.commit()

    return {
        "mensagem": "Produção Apagada",
        "id": id
    }