import click
import logging
LOG_LEVEL = ["DEBUG", "INFO", "WARN", "ERROR", "CRITICAL"]

logger = logging.getLogger(__name__)


@click.group()
@click.option("--main_param_str", required=True, type=str)
@click.option("--main_param_int", required=True, type=int)
@click.option('--main_param_bool', default=False, is_flag=True)
@click.pass_context
def cli(ctx, main_param_bool, main_param_str, main_param_int):
    ctx.ensure_object(dict)
    ctx.obj['MAIN_PARAM_BOOL'] = main_param_bool
    ctx.obj['MAIN_PARAM_STR'] = main_param_str
    ctx.obj['MAIN_PARAM_INT'] = main_param_int


    # parse log level
    numeric_level = getattr(logging, args.log.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level")

    # この モジュールの ログレベルを設定
    logger.setLevel(numeric_level)

    # 標準出力(コンソール)にログを出力するハンドラを生成する
    stream_h = logging.StreamHandler(sys.stdout)
    fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", "%Y-%m-%dT%H:%M:%S")
    stream_h.setFormatter(fmt)
    # ハンドラをロガーに紐づける
    logger.addHandler(stream_h)

    logger.debug(f"{args=}")


@cli.command()
@click.pass_context
@click.option("--sub_param", type=str)
def sub(ctx, sub_param):
    click.echo('start sub')

    click.echo(ctx.obj['MAIN_PARAM_BOOL'])
    click.echo(ctx.obj['MAIN_PARAM_STR'])
    click.echo(ctx.obj['MAIN_PARAM_INT'])
    click.echo(sub_param)


if __name__ == '__main__':
    cli(obj={})
