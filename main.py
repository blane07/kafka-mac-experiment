import faust


app = faust.App('app', broker='kafka://localhost:9092')


class SimpleRecord(faust.Record):
    name: str


@app.agent(value_type = SimpleRecord)
async def display(records):
    async for record in records:
        print(record)


display()

