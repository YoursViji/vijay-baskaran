"use client";

import { useState } from "react";
import { FileText, Menu, X } from "lucide-react";

import { buttonVariants } from "@/components/ui/button";
import { LinkedinMark } from "@/components/linkedin-mark";
import { nav, profile } from "@/lib/profile";
import { cn } from "@/lib/utils";

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
              {profile.name}
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
            <a
              href={profile.linkedin.href}
              target="_blank"
              rel="noreferrer"
              className={cn(
                buttonVariants({ variant: "ghost", size: "icon" }),
                "text-zinc-300"
              )}
              aria-label="LinkedIn"
            >
              <LinkedinMark className="size-4" />
            </a>
            <a
              href={profile.resumeHref}
              target="_blank"
              rel="noreferrer"
              className={cn(
                buttonVariants({ size: "sm" }),
                "hidden sm:inline-flex"
              )}
            >
              <FileText data-icon="inline-start" />
              Resume
            </a>
            <a
              href={profile.guideHref}
              target="_blank"
              rel="noreferrer"
              className={cn(
                buttonVariants({ variant: "outline", size: "sm" }),
                "hidden sm:inline-flex border-white/15 bg-white/4 text-zinc-100"
              )}
            >
              Interview guide
            </a>

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
            <a
              href={profile.resumeHref}
              target="_blank"
              rel="noreferrer"
              className="mt-1 rounded-md bg-cyan-300 px-2 py-3 text-center text-base font-medium text-slate-950"
              onClick={() => setOpen(false)}
            >
              View resume
            </a>
            <a
              href={profile.guideHref}
              target="_blank"
              rel="noreferrer"
              className="rounded-md px-2 py-3 text-center text-base text-zinc-200 hover:bg-white/5 hover:text-cyan-200"
              onClick={() => setOpen(false)}
            >
              Interview guide
            </a>
          </nav>
        </div>
      ) : null}
    </header>
  );
}
