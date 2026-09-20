import { profile } from "@/lib/profile";

export function SiteFooter() {
  return (
    <footer className="border-t border-white/8 py-8">
      <div className="mx-auto flex max-w-6xl flex-col gap-2 px-4 text-sm text-zinc-500 sm:flex-row sm:items-center sm:justify-between sm:px-6">
        <p>
          {profile.name} · {profile.company.legalName}
        </p>
        <p>Kuala Lumpur · Retailetics · TAN Intelligence</p>
      </div>
    </footer>
  );
}
