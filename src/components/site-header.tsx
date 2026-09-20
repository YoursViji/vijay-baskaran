"use client";

import { useState } from "react";
import { Menu, X } from "lucide-react";

import { nav } from "@/lib/profile";

export function SiteHeader() {
  const [open, setOpen] = useState(false);

  function goTo(href: string) {
    setOpen(false);
    window.setTimeout(() => {
      document.querySelector(href)?.scrollIntoView({
        behavior: "smooth",
        block: "start",
      });
      history.replaceState(null, "", href);
    }, 120);
  }

  return (
    <header className="sticky top-0 z-50">
      <div className="border-b border-white/8 bg-[#071018]/90 backdrop-blur-xl">
        <div className="mx-auto flex h-16 max-w-6xl items-center justify-between gap-4 px-4 sm:px-6">
          <a
            href="#top"
            className="flex items-center gap-3"
            onClick={() => setOpen(false)}
          >
            <span className="grid size-9 place-items-center rounded-lg border border-cyan-400/30 bg-cyan-400/10 font-heading text-xs font-semibold tracking-[0.18em] text-cyan-200">
              VB
            </span>
            <span className="hidden font-heading text-sm tracking-tight text-zinc-100 sm:block">
              Vijay Baskaran
            </span>
          </a>

          <nav
            className="hidden items-center gap-0.5 lg:flex"
            aria-label="Primary"
          >
            {nav.map((item) => (
              <a
                key={item.href}
                href={item.href}
                className="rounded-md px-2.5 py-2 text-sm text-zinc-400 transition-colors hover:text-cyan-200"
              >
                {item.label}
              </a>
            ))}
          </nav>

          <div className="flex items-center gap-2">
            <button
              type="button"
              className="inline-flex size-8 items-center justify-center rounded-lg border border-white/15 bg-white/5 text-zinc-100 lg:hidden"
              aria-expanded={open}
              aria-controls="mobile-nav"
              onClick={() => setOpen((value) => !value)}
            >
              {open ? <X className="size-4" /> : <Menu className="size-4" />}
              <span className="sr-only">
                {open ? "Close menu" : "Open menu"}
              </span>
            </button>
          </div>
        </div>
      </div>

      {open ? (
        <div
          id="mobile-nav"
          className="border-b border-white/10 bg-[#0b1620] lg:hidden"
        >
          <nav
            className="mx-auto flex max-w-6xl flex-col gap-1 px-4 py-3 sm:px-6"
            aria-label="Mobile"
          >
            {nav.map((item) => (
              <a
                key={item.href}
                href={item.href}
                className="rounded-md px-2 py-3 text-base text-zinc-200 hover:bg-white/5 hover:text-cyan-200"
                onClick={(event) => {
                  event.preventDefault();
                  goTo(item.href);
                }}
              >
                {item.label}
              </a>
            ))}
          </nav>
        </div>
      ) : null}
    </header>
  );
}
