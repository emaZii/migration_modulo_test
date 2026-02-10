# -*- coding: utf-8 -*-
import logging

_logger = logging.getLogger(__name__)

def migrate(cr, version):
    # Trasformiamo i nomi tecnici di Odoo in nomi di tabelle Postgres (sostituendo il punto con l'underscore)
    old_table = 'test_vecchia_tabella'
    new_table = 'test_nuova_tabella'

    # 1. Rinominiamo la tabella fisica nel DB
    _logger.info(f"Rinomino tabella da {old_table} a {new_table}")
    cr.execute(f"ALTER TABLE {old_table} RENAME TO {new_table}")

    # 2. Aggiorniamo i riferimenti interni di Odoo
    # Questo evita che Odoo pensi che il vecchio modello sia sparito
    cr.execute("UPDATE ir_model SET model = %s WHERE model = %s", (new_table.replace('_', '.'), old_table.replace('_', '.')))
    cr.execute("UPDATE ir_model_data SET model = %s WHERE model = %s", (new_table.replace('_', '.'), old_table.replace('_', '.')))