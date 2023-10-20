import click
from typing import List

def validate_file_type(allowed_extensions: List[str]):
    def callback(ctx, param, value:str):
        if value is not None:
            file_extension = value.lower().rsplit(".", 1)[-1]
            if file_extension not in allowed_extensions:
                raise click.BadParameter(f"File extension should be within the following options: {', '.join(allowed_extensions)}")
        return value
    return callback