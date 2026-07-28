from supabase import create_client
import os


SUPABASE_URL = https://iqsgusmmtjnngetqtlie.supabase.co/rest/v1/

SUPABASE_KEY = sb_publishable_tRzZDpG8Z6yEEH_MvaqHfA_dfkGnzRc


supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)


# Example:

# response = supabase.table("transactions").select("*").execute()
