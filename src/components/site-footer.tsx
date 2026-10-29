import { profile } from "@/lib/profile";

export function SiteFooter() {
  return (
    <footer className="border-t border-white/8 py-8">
      <div className="mx-auto flex max-w-6xl flex-col gap-2 px-4 text-sm text-zinc-500 sm:flex-row sm:items-center sm:justify-between sm:px-6">
        <p>
          {profile.name} · {profile.company.legalName}
        </p>
        <p>
          <a
            href={profile.github.href}
            className="text-zinc-400 underline-offset-4 hover:text-cyan-200 hover:underline"
            target="_blank"
            rel="noreferrer"
          >
            {profile.github.label}
          </a>
        </p>
      </div>
    </footer>
  );
}
