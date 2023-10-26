const std = @import("std");

pub fn main() !void {
    var args = std.process.args();
    _ = args.skip();
    var floors: i32 = 0;
    if (args.next()) |arg| {
        for (arg) |c| {
            switch (c) {
                '(' => floors += 1,
                ')' => floors -= 1,
                else => unreachable,
            }
        }
    }
    std.debug.print("floors: {}\n", .{floors});
}
