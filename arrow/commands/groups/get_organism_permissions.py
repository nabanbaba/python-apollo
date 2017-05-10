import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('get_organism_permissions')
@click.argument("group", type=str)


@pass_context
@apollo_exception
@dict_output
def cli(ctx, group):
    """Get the group's organism permissions
    """
    return ctx.gi.groups.get_organism_permissions(group)