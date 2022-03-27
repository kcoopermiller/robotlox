use rlua::{Lua, Result};
use std::fs::File;
use std::io::{BufReader, Read};
use std::path::Path;

fn main() {
    lua().unwrap();
}

pub fn lua() -> Result<()> {
    let mut reader: BufReader<File> =
        BufReader::new(File::open(Path::new("src/roblox/src/server/init.server.lua")).unwrap());
    let mut lua_source: String = String::new();

    reader.read_to_string(&mut lua_source);

    let lua = Lua::new();
    lua.context(|lua_ctx| {
        lua_ctx.load(&lua_source).exec()?;
        Ok(())
    })?;

    Ok(())
}
