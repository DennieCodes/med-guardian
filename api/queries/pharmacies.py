from pydantic import BaseModel
from typing import Union, List, Optional
from models.pharmacies import PharmacyIn, PharmacyOut, Error
from queries.pool import pool


class PharmacyRepository(BaseModel):
    # CREATE
    def create(self, pharmacy: PharmacyIn, account_id: int):
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT into pharmacies
                            (name, phone, address, website, user_id)
                        VALUES
                            (%s, %s, %s, %s, %s)
                        RETURNING id;
                        """,
                        [
                            pharmacy.name,
                            pharmacy.phone,
                            pharmacy.address,
                            pharmacy.website,
                            account_id
                        ]
                    )
                    id = result.fetchone()[0]
                    return self.pharmacy_in_to_out(id, pharmacy, account_id)

        except Exception as e:
            print(e)
            return {
                "message":
                "Could not enter a new pharmacy entry into the system"}

    # UPDATE
    def update(self, pharmacy_id: int, pharmacy: PharmacyIn):
        try:
            with pool.connection as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE pharmacies
                        SET name = %s
                          , phone = %s
                          , address = %s
                          , website = %s
                        WHERE id = %s
                        """,
                        [
                            pharmacy.name,
                            pharmacy.phone,
                            pharmacy.address,
                            pharmacy.website,
                            pharmacy.id
                        ]
                    )
                    # This will require authenticator to pass in user_id
                    return self.pharmacy_in_to_out(pharmacy_id, pharmacy, None)

        except Exception as e:
            print(e)
            return {"message": "Could not update that pharmacy record"}

    # DELETE
    def delete(self, pharmacy_id: int):
        try:
            with pool.connection as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM pharmacies
                        WHERE id = %s
                        """,
                        [pharmacy_id]
                    )
                    return True

        except Exception as e:
            print(e)
            return False

    # GET_ONE
    def get_one(self, pharmacy_id: int) -> Optional[PharmacyOut]:
        try:
            with pool.connection as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id
                             , name
                             , phone
                             , address
                             , website
                             , user_id
                        FROM pharmacies
                        WHERE id = %s
                        """,
                        [pharmacy_id]
                    )
                    record = result.fetchone()

                    if record is None:
                        return None
                    return self.record_to_pharmacy_out(record)

        except Exception as e:
            print(e)
            return {"message": "Could not get that pharmacy's information"}

    # GET_ALL
    def get_all(self) -> Union[Error, List[PharmacyOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, name, phone, address, website, user_id
                        FROM pharmacies
                        """
                    )

                    return [
                        self.record_to_pharmacy_out(record)
                        for record in result
                    ]
        except Exception as e:
            print(e)
            return {"message": "Could not get list of all pharmacies"}

    def pharmacy_in_to_out(self, id: int, pharmacy: PharmacyIn, user_id: int):
        old_data = pharmacy.dict()
        return PharmacyOut(id=id, **old_data, user_id=user_id)

    def record_to_pharmacy_out(self, record):
        print("RECORD: ", record)
        return PharmacyOut(
            id=record[0],
            name=record[1],
            phone=record[2],
            address=record[3],
            website=record[4],
            user_id=record[5]
        )
